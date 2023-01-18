
from app import db
from app.models.base import BaseModel


class ChildKinship(db.Model, BaseModel):
    __tablename__ = "child_kinship"

    kinship = db.Column(db.String(255))
    parent_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"))

    def create_item(self, model_dict):
        self.parent_id = model_dict['parent_id']
        self.child_id = model_dict['child_id']
        self.kinship = model_dict['kinship']
        return self

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
