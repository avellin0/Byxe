from flask import Flask, request, Response
import subprocess

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get('url')

    if not video_url:
        return "URL do vídeo é obrigatória.", 400

    # Comando para baixar o vídeo usando yt-dlp e enviar para stdout
    command = ['yt-dlp', '-o', '-', video_url]

    # Executa o comando e faz streaming diretamente para a resposta HTTP
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def generate():
        try:
            while True:
                data = process.stdout.read(1024)
                if not data:
                    break
                yield data
        finally:
            process.stdout.close()

    return Response(generate(), mimetype='video/mp4',
                    headers={"Content-Disposition": "attachment; filename=video.mp4"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
