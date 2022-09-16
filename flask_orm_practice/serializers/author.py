from marshmallow import Schema, fields
from marshmallow.validate import Length


class AuthorSchema(Schema):
    id = fields.Integer(primary_key=True, autoincrement=True)
    name = fields.String(nullable=False, unique=True, validate=Length(min=2, max=30))
    age = fields.Integer(nullable=False)
