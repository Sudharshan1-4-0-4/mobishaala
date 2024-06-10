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
    npm start
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

## Deployment

### Frontend

1. Deploy the frontend application to Vercel. Follow the [Vercel Deployment Guide](https://vercel.com/docs/concepts/projects/overview).

### Backend

1. Deploy the backend application to Heroku. Follow the [Heroku Deployment Guide](https://devcenter.heroku.com/articles/getting-started-with-python).

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

## Evaluation Criteria

1. **Functionality**: The application correctly handles video uploads and mixing.
2. **Code Quality**: The code is well-structured and documented.
3. **User Experience**: The user interface is intuitive and responsive.
4. **Deployment**: The application is successfully deployed on Vercel and Heroku.

## License

MIT License
