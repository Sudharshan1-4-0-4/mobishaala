import React from 'react';
import { useDropzone } from 'react-dropzone';

const VideoUpload = ({ onUpload }) => {
  const { getRootProps, getInputProps } = useDropzone({
    accept: 'video/*',
    onDrop: (acceptedFiles) => onUpload(acceptedFiles),
  });

  return (
    <div {...getRootProps({ className: 'dropzone' })}>
      <input {...getInputProps()} />
      <p>Drag 'n' drop some videos here, or click to select videos</p>
    </div>
  );
};

export default VideoUpload;
