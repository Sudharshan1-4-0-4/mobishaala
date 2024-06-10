# mobishaala

# VidMix - Video Mixing Application

## Overview
VidMix is a web application that allows users to upload two input videos and mix them into a single video. The mixed video displays both input videos side by side, each occupying 50% of the container area.

## Technology Stack
- **Frontend**: React
- **Backend**: Python with Flask
- **Database**: MongoDB
- **Video Processing**: FFmpeg
- **Storage**: Local file storage


## Setup Instructions

### Frontend

1. Install dependencies
    ```bash
    npm install
    ```

2. Run the React application
    ```bash
    npm run dev
    ```

### Backend

1. Create a virtual environment
    ```bash
    python -m venv venv
    venv/bin/activate
    ```

2. Install dependencies
    ```bash
    pip install flask pymongo flask_pymongo flask_cors moviepy
    ```

3. Run the Flask application
    ```bash
    python app.py
    ```


## Usage

1. Upload two videos using the drag-and-drop interface.
2. Click "Mix Videos" to mix the uploaded videos.
3. Preview and download the mixed video.

## Code Quality

- The code is well-structured and documented.
- Best practices are followed in terms of API design and frontend-backend integration.

## User Experience

- The user interface is intuitive and responsive.
- The video mixing process is efficient and error-free.
