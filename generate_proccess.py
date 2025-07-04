import os
from text_to_audio import text_to_speech_file
import time
import subprocess
ffmpeg_cwd = os.getcwd()
def text_to_audio(folder):
    print("TTA -", folder)
    desc_file_path = f"user_uploads/{folder}/desc.txt"
    
    if os.path.exists(desc_file_path):
        with open(desc_file_path, "r") as f:
            text = f.read()
            print(text, folder)
            # Uncomment the next line to actually generate audio
            text_to_speech_file(text, folder)
    else:
        print(f"desc.txt not found in {folder}")



# def create_reel(folder):
#     command = f'ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -pix_fmt yuv420p -shortest static/reels/{folder}.mp4'
#     print(f"Running ffmpeg for folder: {folder}")

#     subprocess.run(command, shell=True, check=True)
def create_reel(folder):
    input_txt = f"user_uploads/{folder}/input.txt"
    audio_file = f"user_uploads/{folder}/audio.mp3"
    output_file = f"static/reels/{folder}.mp4"

    if not os.path.exists(input_txt):
        raise FileNotFoundError(f"{input_txt} is missing")
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"{audio_file} is missing")

    command = f'ffmpeg -f concat -safe 0 -i "{input_txt}" -i "{audio_file}" -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -pix_fmt yuv420p -shortest "{output_file}"'
    print(f"Running ffmpeg for folder: {folder}")
    subprocess.run(command, shell=True, check=True)




if __name__ == "__main__":
    # Read already processed folders
    while True:
        print('PROCESSING QUEUE')
        if os.path.exists("done.txt"):
            with open("done.txt", "r") as f:
                done_folders = [line.strip() for line in f.readlines()]
        else:
            done_folders = []

        # Get folders from user_uploads
        folders = os.listdir("user_uploads")

        for folder in folders:
            if folder not in done_folders:
                text_to_audio(folder)
                create_reel(folder)
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)


