from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class ChildSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    birth_date = fields.Date()
    status = fields.Boolean()
    team_id = fields.Int(load_only=True)

    team = fields.Nested('TeamSchema', exclude=('created_at', 'updated_at'), dump_only=True)
    parents = fields.Nested('UserSchema', only=('id', 'name'), many=True, dump_only=True)
    
    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
