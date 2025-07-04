# AI-reel-generator
This project is a simple web app that lets you convert image files into video files. It’s built with Flask, a web framework that takes care of handling the file uploads and running the conversion, and uses FFmpeg to turn your images into .mp4 files.

What It Does: Flask App (main.py): It handles everything behind the scenes—when you upload the images, it saves the file, converts it to video using FFmpeg and your text to audio using elevenlabs.

Front-End: The user interface (created with HTML, CSS, JavaScript) is where you interact with the app. You can drag and drop your images or select them manually, then you have to enter the text which you want convert into audio with the help of elevenlabs, then click on create reel.

How It Works: Upload Your Images: You can either drag your image file onto the webpage or select it using the file picker.
Download Your Reel: Once the conversion is complete, you can check out your reel in the gallery.

Dependencies:Flask,FFmpeg,Python,elevenlabs.
