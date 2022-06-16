from flask import request
from flask_restx import Resource, Namespace

from project.schemas.users import UsersSchema
from project.container import user_service

user_ns = Namespace('user')


@user_ns.route("/<int:uid>")
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UsersSchema().dump(user)
        return result, 200

    def patch(self, uid):
        data = request.get_json()
        user_service.update_part(data, uid)
        return '', 204
