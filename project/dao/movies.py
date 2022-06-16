from project.dao.models import Movies


class MoviesDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movies).get(mid)

    def get_all(self):
        return self.session.query(Movies).all()
    



