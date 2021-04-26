from flask import render_template
from application.model.entity.video import Video
from application.model.dao.categoria_dao import CategoriaDAO
from application import app

@app.route("/video/<int:id>")
def video(id: int):
    video = CategoriaDAO().find_video_by_id(id)
    return render_template("video.html", video=video)
    