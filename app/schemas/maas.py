from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class MaasSchema(BaseSchema):
    position = fields.Int()
    name = fields.Str()
    slug = fields.Str()
    description = fields.Str()
    status = fields.Boolean()

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
