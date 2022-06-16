from project.dao.models.directors import Directors


class DirectorsDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Directors).get(bid)

    def get_all(self):
        return self.session.query(Directors).all()
