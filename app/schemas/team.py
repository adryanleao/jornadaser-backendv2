from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class TeamSchema(BaseSchema):
    name = fields.Str(required=True)
    module = fields.Str()
    status = fields.Boolean()
    institution_id = fields.Int()
    teacher_id = fields.Int(load_only=True)
    teacher = fields.Nested('UserSchema', only=('id', 'name'), dump_only=True)
    institution = fields.Nested('InstitutionSchema', only=('id', 'name'), dump_only=True)
    students = fields.Nested('UserSchema', many=True, only=('id', 'name'), dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
