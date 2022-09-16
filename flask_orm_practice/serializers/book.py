from marshmallow import Schema, fields
from marshmallow.validate import Length

from serializers.author import AuthorSchema


class BookSchema(Schema):
    id = fields.Integer(primary_key=True, autoincrement=True)
    name = fields.String(nullable=False, unique=True, validate=Length(min=1, max=50))
    description = fields.String(nullable=False, validate=Length(min=1, max=50))
    author_id = fields.Integer(required=False)
    author = fields.Nested(AuthorSchema)
