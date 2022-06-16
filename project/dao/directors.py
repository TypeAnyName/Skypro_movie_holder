from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.directors import Directors


class DirectorsDao:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(Directors).filter(Directors.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(Directors).all()