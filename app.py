import os

from flask import Flask, render_template

from config import config_por_ambiente
from extensions import db, migrate, login_manager, csrf


def create_app(ambiente=None):
    ambiente = ambiente or os.environ.get("FLASK_ENV", "development")

    app = Flask(__name__)
    app.config.from_object(config_por_ambiente[ambiente])

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    @app.route("/")
    def inicio():
        return render_template("index.html")

    @app.route("/cadastro")
    def cadastro():
        return render_template("cadastro.html")

    @app.route("/medicamentos")
    def medicamentos():
        return render_template("medicamentos.html")

    @app.route("/login")
    def login():
        return render_template("login.html")

    return app


if __name__ == "__main__":
    create_app().run()