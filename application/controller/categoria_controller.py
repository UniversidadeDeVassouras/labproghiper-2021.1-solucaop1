from flask import render_template
from application.model.entity.categoria import Categoria
from application.model.dao.categoria_dao import CategoriaDAO
from application import app

@app.route("/")
def home():
    categoria_list = CategoriaDAO().find_all()
    return render_template("home.html", categoria_list = categoria_list)