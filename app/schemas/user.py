from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class UserSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    email = fields.Str()
    password = fields.Str(load_only=True)
    name = fields.Str(required=True)
    taxpayer = fields.Str()
    genre = fields.Str()
    cell_phone = fields.Str()
    birth_date = fields.DateTime()
    status = fields.Boolean()

    group_id = fields.Int(load_only=True)

    group = fields.Nested('GroupSchema',
                          exclude=('created_at', 'updated_at'), dump_only=True)
    address = fields.Nested('AddressSchema', exclude=('created_at', 'updated_at'))
    
    institutions = fields.Nested('InstitutionSchema', many=True,
                              exclude=('created_at', 'updated_at'), dump_only=True)
    
    secretaries = fields.Nested('SecretarySchema', many=True,
                              exclude=('created_at', 'updated_at'), dump_only=True)
    
    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
