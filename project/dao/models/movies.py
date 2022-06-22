from project.setup_db import db


class Movies(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))

    def __repr__(self):
        return f"<Movie '{self.title.title()}'>"
