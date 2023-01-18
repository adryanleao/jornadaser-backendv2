import uuid
from app import db

from app.models.base import BaseModel


class SchoolClass(db.Model, BaseModel):
    __tablename__ = "school_class"

    hash_id = db.Column(db.String(36), unique=True, nullable=False, default=lambda x: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean(), nullable=False, default=1)


    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
