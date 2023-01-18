import uuid
from app import db

from app.models.base import BaseModel
from app.services.aws.s3 import get_aws_image_keys


class Content(db.Model, BaseModel):
    __tablename__ = "content"

    hash_id = db.Column(db.String(36), unique=True, nullable=False, default=lambda x: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Boolean(), nullable=False, default=1)

    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
