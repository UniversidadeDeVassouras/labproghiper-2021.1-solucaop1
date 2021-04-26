from flask import Flask, render_template
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria
from application.model.dao.categoria_dao import CategoriaDAO
import os

app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

@app.route("/")
def home():
    categoria_list = CategoriaDAO().find_all()
    return render_template("home.html", categoria_list = categoria_list)
 
@app.route("/video/<int:id>")
def video(id: int):
    video = CategoriaDAO().find_video_by_id(id)
    return render_template("video.html", video=video)
    
