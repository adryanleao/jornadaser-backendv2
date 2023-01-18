from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class SecretaryMaasRatingSchema(BaseSchema):
    rating = fields.Str()
    maas_id = fields.Int(dump_only=True)
    secretary_id = fields.Str(dump_only=True)
    status = fields.Boolean()

    maas = fields.Nested('MaasSchema', many=True,
                         exclude=('created_at', 'updated_at'))

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
