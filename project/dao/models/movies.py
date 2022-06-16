from project.setup_db import db


class Movies(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer)
    director_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<Movie '{self.title.title()}'>"
