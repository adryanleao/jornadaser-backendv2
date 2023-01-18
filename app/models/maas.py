from app import db
from app.models.base import BaseModel


# The UserAddress class has a one-to-one relationship with the User class and a one-to-one
# relationship with the City class
class Maas(db.Model, BaseModel):
    __tablename__ = "maas"

    position = db.Column(db.Integer)
    name = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    description = db.Column(db.String(255))
    status = db.Column(db.Boolean(), nullable=False, default=1)

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
