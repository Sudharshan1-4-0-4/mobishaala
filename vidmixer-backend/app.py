from flask import Flask, request, send_from_directory, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from moviepy.editor import VideoFileClip, clips_array
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/vidmixer"
mongo = PyMongo(app)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return "Welcome to the VidMix API!"

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'video1' not in request.files or 'video2' not in request.files:
        return 'No file part', 400
    video1 = request.files['video1']
    video2 = request.files['video2']
    if video1.filename == '' or video2.filename == '':
        return 'No selected file', 400
    filename1 = secure_filename(video1.filename)
    filename2 = secure_filename(video2.filename)
    video1_path = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
    video2_path = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
    video1.save(video1_path)
    video2.save(video2_path)
    mixed_video_path = mix_videos(video1_path, video2_path)
    video_entry = {
        'video1_path': video1_path,
        'video2_path': video2_path,
        'mixed_video_path': mixed_video_path
    }
    mongo.db.videos.insert_one(video_entry)
    return jsonify({'mixedVideoUrl': os.path.basename(mixed_video_path)})

def mix_videos(video1_path, video2_path):
    clip1 = VideoFileClip(video1_path)
    clip2 = VideoFileClip(video2_path)
    mixed_clip = clips_array([[clip1, clip2]])
    mixed_video_path = os.path.join(app.config['UPLOAD_FOLDER'], f"mixed_{os.path.basename(video1_path)}")
    mixed_clip.write_videofile(mixed_video_path, codec="libx264", fps=24)
    return mixed_video_path

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
