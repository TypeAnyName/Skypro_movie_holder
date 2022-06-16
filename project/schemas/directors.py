from marshmallow import Schema, fields


class DirectorsSchema(Schema):
    id = fields.Int()
    name = fields.Str()
