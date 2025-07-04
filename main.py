from flask import Flask, render_template, request
import uuid
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ffmpeg_cwd = os.getcwd()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=['GET', 'POST'])
def create():
    myid = str(uuid.uuid1())  # generate once per form
    user_folder = os.path.join(app.config['UPLOAD_FOLDER'], myid)
    os.makedirs(user_folder, exist_ok=True)
    input_files = []

    if request.method == 'POST':
        print(request.files.keys())
        print(request.form.get("uuid"))
        print(request.form.get("text"))

        for key in request.files:
            file = request.files[key]
            if file and file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join(user_folder, filename))
                input_files.append(filename)

        text = request.form.get("text", "")
        with open(os.path.join(user_folder, "desc.txt"), "w") as f:
            f.write(text)

        for fl in input_files:
            with open(os.path.join(user_folder, "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")

    


    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html",reels=reels)

app.run(debug=True)