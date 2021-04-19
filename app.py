from flask import Flask, render_template
from video import Video
from categoria import Categoria

app = Flask(__name__)

video_streetfighter = Video(1, 'Street Fighter', 'Vídeo do Street Fighter', 'img/stf1.jpg', 'video/stf1.mp4')
video_naturo = Video(2, 'Naturo', 'Vídeo de Naruto', 'img/shonen1.jpg', 'video/shonen1.webm')
video_desaf_gigantes = Video(3, 'Desafiando Gigantes', 'Vídeo Desafiando Gigantes', 'img/capa_desafiandogigantes.png', 'video/desafiando-gigantes.mp4')
video_mr_sunshine = Video(4, 'Mr. Sunshine', 'Vídeo Mr. Sunshine', 'img/capa_mrsunshine.png', 'video/desafiando-gigantes.mp4')

categoria_anime = Categoria(1, 'Animes', [video_streetfighter, video_naturo])
categoria_filme_inter = Categoria(2, 'Filmes Internacionais', [video_mr_sunshine, video_desaf_gigantes])

categorias = [categoria_anime, categoria_filme_inter]

@app.route("/")
def home():
    return render_template("home.html", categoria_list = categorias)
