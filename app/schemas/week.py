from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class WeekSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Boolean()

    category_id = fields.Int(load_only=True)
    school_class_id = fields.Int(load_only=True)
    
    category = fields.Nested('CategorySchema', dump_only=True)
    school_class = fields.Nested('SchoolClassSchema', dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
