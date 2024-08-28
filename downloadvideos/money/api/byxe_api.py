from flask import Flask,request,send_file,jsonify,Response
import yt_dlp
import requests
from flask_cors import CORS
import subprocess
import os


app = Flask(__name__)

CORS(app)

@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get('url')

    if not video_url:
        return "URL do vídeo é obrigatória.", 400

    # Comando para baixar o vídeo usando yt-dlp e enviar para stdout
    command = ['yt-dlp', '-o', '-', video_url]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def generate():
        while True:
            data = process.stdout.read(1024)
            if not data:
                break
            yield data

    return Response(generate(), mimetype='video/mp4', headers={"Content-Disposition": "attachment; filename=video.mp4"})


@app.route('/send', methods=['GET'])
def sendImage():    
    image_file = request.args.get('url')

    if not image_file:
        return "url não fornecida"
    
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info_dict = ydl.extract_info(image_file, download=False)

        thumb_url = info_dict.get('thumbnail')
        response = requests.get(thumb_url)

        if thumb_url:
            return Response(response.content, mimetype=response.headers['content-type'])
        else:
            return jsonify({"error": "Thumbnail não encontrada."}), 404


app.run(port=5000,host="localhost",debug=True)