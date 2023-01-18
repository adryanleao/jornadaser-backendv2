from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class InstitutionSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    site = fields.Str()
    cell_phone = fields.Str()
    responsible = fields.Str()
    responsible_phone = fields.Str()
    email = fields.Str()
    function = fields.Str()
    type = fields.Str()
    status = fields.Boolean()
    secretary_id = fields.Int(load_only=True)

    address = fields.Nested('InstitutionAddressSchema', many=False,
                              exclude=('created_at', 'updated_at'))
    
    secretary = fields.Nested('SecretarySchema', many=False, dump_only=True,
                              exclude=('created_at', 'updated_at'))

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
