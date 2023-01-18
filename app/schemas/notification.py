from marshmallow import EXCLUDE, fields

from app.schemas.base import BaseSchema


class NotificationSchema(BaseSchema):
    hash_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    user_type = fields.Str()
    team = fields.Str()
    status = fields.Boolean()

    institution_id = fields.Int(laod_only=True)

    institution = fields.Nested('InstitutionSchema', many=True,
                                exclude=('created_at', 'updated_at'), dump_only=True)

    class Meta:
        unknown = EXCLUDE
        exclude = ('created_at', 'updated_at')
