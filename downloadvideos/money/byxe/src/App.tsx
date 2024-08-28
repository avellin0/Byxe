import './App.css'
import { useState} from 'react'

export const Home = () => {
  const [url, setUrl] = useState("");
  const [imgSrc, setImgSrc] = useState("");
  const [text, setText] = useState("search");
  // const [videoLink, setVideoLink] = useState<string>("");

  const getImage = async () => {
    if (text === "Baixar") {
      const response = await fetch(`http://localhost:5000/download?url=${url}`);
      if (!response.ok) {
        throw new Error("Vídeo não encontrado");
      }

      const videoBlob = await response.blob();
      const videoUrl = URL.createObjectURL(videoBlob);

      const a = document.createElement('a')
      a.href = videoUrl
      a.download = 'video.mp4'
      document.body.appendChild(a)
      a.click();
      document.body.removeChild(a)

      // setVideoLink(videoUrl); // Armazena o link para download
      
      return setText("search");
    }

    const response = await fetch(`http://localhost:5000/send?url=${url}`);
    if (!response.ok) {
      throw new Error('não achei essa merda');
    }

    const blob = await response.blob();
    const imgUrlTemp = URL.createObjectURL(blob);
    setImgSrc(imgUrlTemp);
    setText("Baixar");
  };

  return (
    <>
    <div className="home-body">
      <div className="search-area">
        <input
          type="text"
          id="home-search-url"
          onChange={(e) => setUrl(e.target.value)}
        />
        <button value="enviar" id="home-search-btn" onClick={getImage}>
          {text}
        </button>
      </div>

      <div className="home-image-area">
        <img src={imgSrc} id="home-img" alt="" />
      </div>
    </div>
  </>
  );
};
