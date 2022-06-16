from flask import Flask
from flask_restx import Api


from project.views.directors import directors_ns
from project.views.genres import genres_ns
from project.views.movies import movie_ns
from project.config import BaseConfig
from project.setup_db import db


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)


if __name__ == '__main__':
    app_config = BaseConfig()
    app = create_app(app_config)
    app.run()
