import uuid

from app import db, models
from app.models.base import BaseModel


class Child(db.Model, BaseModel):
    __tablename__ = "child"

    hash_id = db.Column(db.String(36), unique=True,
                        nullable=False, default=lambda x: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date)
    status = db.Column(db.Boolean(), nullable=False, default=1)

    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))

    team = db.relationship('Team', backref='team', lazy=True,
                           uselist=False, foreign_keys=[team_id])

    def _get_parents(self):
        return models.ChildKinship.query.join(
            models.User,
            models.User.id == models.ChildKinship.parent_id
        ).with_entities(
            models.User.id,
            models.User.name,
            models.ChildKinship.child_id,
            models.ChildKinship.deleted_at,
            models.User
        ).filter(
            models.ChildKinship.child_id == self.id,
            models.ChildKinship.deleted_at.is_(None),
            models.User.deleted_at.is_(None)
        ).all()

    parents = property(_get_parents)

    def create_item(self, dict_model):
        self.name = dict_model.get("name", self.name)
        self.birth_date = dict_model.get("birth_date", self.birth_date)
        self.status = dict_model.get("status", self.status)
        self.team_id = dict_model.get("team_id", self.team_id)

        return self

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)


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
