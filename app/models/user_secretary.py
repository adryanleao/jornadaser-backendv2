from app import db
from app.models.base import BaseModel


class UserSecretary(db.Model, BaseModel):
    __tablename__ = "user_secretary"

    # foreign key
    secretary_id = db.Column(db.Integer, db.ForeignKey("secretary.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def create_item(self, model_dict):
        self.user_id = model_dict['user_id']
        self.secretary_id = model_dict['secretary_id']
        return self

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
