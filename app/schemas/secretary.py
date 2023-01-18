from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema
from app.services import spec


class SecretarySchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    organ = fields.Str(required=True)
    site = fields.Str()
    cell_phone = fields.Str()
    responsible = fields.Str()
    responsible_phone = fields.Str()
    email = fields.Str()
    function = fields.Str()
    image_key = fields.Str()
    status = fields.Boolean()

    address = fields.Nested('SecretaryAddressSchema',
                            exclude=('created_at', 'updated_at'))

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
