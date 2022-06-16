from sqlalchemy.exc import IntegrityError

from project.config import DevelopmentConfig
from project.dao.models import Genre, Directors, Movies

from project.server import create_app
from project.setup_db import db
from project.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("fixtures.json")

with app.app_context():
    for genre in data["genres"]:
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))
    for directors in data["directors"]:
        db.session.add(Directors(id=directors["pk"], name=directors["name"]))
    for movies in data["movies"]:
        db.session.add(Movies(id=movies["pk"],
                              title=movies['title'],
                              description=movies["description"],
                              trailer=movies['trailer'],
                              year=movies['year'],
                              rating=movies["rating"],
                              genre_id=movies['genre_id'],
                              director_id=movies['director_id']))


    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
