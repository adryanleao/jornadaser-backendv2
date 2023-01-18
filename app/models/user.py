import uuid

from app import db, models
from app.models.base import BaseModel

"""
Credential levels

1 - System / Sistema (desenvolvedores)
2 - Admin
3 - Tutor
4 - Professor
5 - Responsável
6 - Aluno
"""


class User(db.Model, BaseModel):
    __tablename__ = "user"

    hash_id = db.Column(db.String(36), unique=True,
                        nullable=False, default=lambda x: str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    email_verified = db.Column(db.Boolean, default=0)
    token_update = db.Column(db.String(36))
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    image_key = db.Column(db.String(255))
    taxpayer = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    cell_phone = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    status = db.Column(db.Boolean(), nullable=False, default=1)

    # foreign key
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    # relationship
    group = db.relationship('Group', backref='user', lazy=True, uselist=False)

    # address
    address = db.relationship('UserAddress', backref='user', lazy=True,
                              uselist=False)

    def _get_institutions(self):
        return models.UserInstitution.query.join(
            models.Institution,
            models.Institution.id == models.UserInstitution.institution_id
        ).with_entities(
            models.Institution.id,
            models.Institution.name,
            models.UserInstitution.user_id,
            models.UserInstitution.deleted_at,
            models.Institution
        ).filter(
            models.UserInstitution.user_id == self.id,
            models.UserInstitution.deleted_at.is_(None),
            models.Institution.deleted_at.is_(None)
        ).all()

    institutions = property(_get_institutions)

    def _get_secretaries(self):
        return models.UserSecretary.query.join(
            models.Secretary,
            models.Secretary.id == models.UserSecretary.secretary_id
        ).with_entities(
            models.Secretary.id,
            models.Secretary.name,
            models.UserSecretary.user_id,
            models.UserSecretary.deleted_at,
            models.Secretary
        ).filter(
            models.UserSecretary.user_id == self.id,
            models.UserSecretary.deleted_at.is_(None),
            models.Secretary.deleted_at.is_(None)
        ).all()

    secretaries = property(_get_secretaries)

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
