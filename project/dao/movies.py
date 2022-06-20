from flask import current_app
from sqlalchemy import desc

from project.dao.models import Movies


class MoviesDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movies).get(mid)

    def get_all(self, page: str = None, sort: bool = False):
        items = self.session.query(Movies)
        if sort:
            items = items.order_by(desc(Movies.year))
        if page:
            items = (items
                     .limit(current_app.config.get("ITEMS_PER_PAGE"))
                     .offset(page * current_app.config.get("ITEMS_PER_PAGE")
                             - current_app.config.get("ITEMS_PER_PAGE")))
        return items.all()




