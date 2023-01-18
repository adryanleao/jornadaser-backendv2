from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class ExtraMaterialSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    type = fields.Str()
    user_type = fields.Str()
    module = fields.Str()
    link = fields.Str()
    file_key = fields.Str()
    status = fields.Boolean()
    
    category_id = fields.Int(laod_only=True)
    school_class_id = fields.Int(laod_only=True)
    institution_id = fields.Int(laod_only=True)

    category = fields.Nested('CategorySchema', exclude=('created_at', 'updated_at'), dump_only=True)
    school_class = fields.Nested('SchoolClassSchema', exclude=('created_at', 'updated_at'), dump_only=True)
    institution = fields.Nested('InstitutionSchema', exclude=('created_at', 'updated_at'), dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
