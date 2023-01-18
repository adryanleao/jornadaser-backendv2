import uuid
from app import db

from app.models.base import BaseModel


class Notification(db.Model, BaseModel):
    __tablename__ = "notification"

    hash_id = db.Column(db.String(36), unique=True, nullable=False, default=lambda x: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    user_type = db.Column(db.String(255))
    team = db.Column(db.String(255))
    status = db.Column(db.Boolean(), nullable=False, default=1)

    # foreign key
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))

    # relationship
    institution = db.relationship(
        'Institution', uselist=False, backref="notification")

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
