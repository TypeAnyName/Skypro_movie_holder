from flask import Flask, render_template
from flask_restx import Api

from project.views.auth import auth_ns
from project.views.directors import directors_ns
from project.views.genres import genres_ns
from project.views.movies import movie_ns
from project.config import BaseConfig
from project.setup_db import db
from project.views.user import user_ns

api = Api(title="Flask Course Project 3", doc="/docs")


def create_app(config_object):
    application = Flask(__name__,
                        template_folder="C:/Users/alexg/PycharmProjects/CW3/templates",
                        static_folder="C:/Users/alexg/PycharmProjects/CW3/static"
                        )
    application.config.from_object(config_object)
    register_extensions(application)

    @application.route('/index/')
    def index():
        return render_template('index.html')

    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


if __name__ == '__main__':
    app_config = BaseConfig()
    app = create_app(app_config)
    app.run(port=25000)
