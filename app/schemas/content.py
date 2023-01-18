from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class ContentSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    status = fields.Boolean()

    week_id = fields.Int(load_only=True)
    
    week = fields.Nested('WeekSchema', dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
