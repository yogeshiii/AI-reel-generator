def create_reel(folder):
    command = f'ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -pix_fmt yuv420p -shortest static/reels/{folder}.mp4'
    print(f"Running ffmpeg for folder: {folder}")
    subprocess.run(command, shell=True, check=True)