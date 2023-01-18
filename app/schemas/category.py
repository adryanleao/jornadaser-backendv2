from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class CategorySchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Boolean()

    image = fields.Nested('ImageSchema')

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
