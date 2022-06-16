from project.container import movie_service
from project.schemas.movies import MoviesSchema
from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        b = movie_service.get_one(mid)
        sm_d = MoviesSchema().dump(b)
        return sm_d, 200