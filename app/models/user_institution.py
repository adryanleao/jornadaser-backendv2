
from app import db
from app.models.base import BaseModel


class UserInstitution(db.Model, BaseModel):
    __tablename__ = "user_institution"

    # foreign key
    institution_id = db.Column(db.Integer, db.ForeignKey("institution.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def create_item(self, model_dict):
        self.user_id = model_dict['user_id']
        self.institution_id = model_dict['institution_id']
        return self

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
