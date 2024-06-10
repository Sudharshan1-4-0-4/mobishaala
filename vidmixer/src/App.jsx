import React, { useState } from 'react';
import VideoUpload from './components/VideoUpload';
import axios from 'axios';
import './App.css';

const App = () => {
  const [videos, setVideos] = useState([]);
  const [mixedVideo, setMixedVideo] = useState(null);

  const handleUpload = (acceptedFiles) => {
    setVideos(acceptedFiles);
  };

  const handleMixVideos = async () => {
    const formData = new FormData();
    videos.forEach((video, index) => {
      formData.append(`video${index + 1}`, video);
    });

    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data);
      console.log(response.data.mixedVideoUrl);
      setMixedVideo(response.data.mixedVideoUrl);
    } catch (error) {
      console.error('Error mixing videos:', error);
    }
  };

  return (
    <div className="App">
      <VideoUpload onUpload={handleUpload} />
      {videos.length === 2 && (
        <button onClick={handleMixVideos}>Mix Videos</button>
      )}
      <div>
      {mixedVideo && (
        <video src={`http://localhost:5000/uploads/${mixedVideo}`} controls width="600"/>
      )}
      </div>
      
    </div>
  );
};

export default App;
