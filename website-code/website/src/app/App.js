import './App.css';
import { Overlay, Video } from '../styles';
import { useRef, useEffect } from 'react';
function App() {
  const vidRef=useRef();

useEffect(() => { vidRef.current.play(); },[]);
  return (
    <Overlay>
      <Video
        src="https://i.imgur.com/KEnwbfZ.mp4"
        ref={ vidRef }
        muted
        autoPlay
        loop 
      />
    </Overlay>
  );
}

export default App;
