import uuid
from app import db

from app.models.base import BaseModel


class Institution(db.Model, BaseModel):
    __tablename__ = "institution"

    hash_id = db.Column(db.String(36), unique=True, nullable=False, default=lambda x: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    site = db.Column(db.String(255))
    cell_phone = db.Column(db.String(255))
    responsible = db.Column(db.String(255))
    responsible_phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    function = db.Column(db.String(255))
    type = db.Column(db.String(255))
    status = db.Column(db.Boolean(), nullable=False, default=1)
    
    secretary_id = db.Column(db.Integer, db.ForeignKey('secretary.id'))

    # address
    address = db.relationship('InstitutionAddress', backref='institution', lazy=True,
                                uselist=False)
    
    secretary = db.relationship('Secretary', backref='institution', lazy=True,
                                uselist=False)

    def create_item(self, dict_model):
        self.name = dict_model.get("name", self.name)
        self.site = dict_model.get("site", self.site)
        self.cell_phone = dict_model.get("cell_phone", self.cell_phone)
        self.responsible = dict_model.get("responsible", self.responsible)
        self.responsible_phone = dict_model.get("responsible_phone", self.responsible_phone)
        self.email = dict_model.get("email", self.email)
        self.function = dict_model.get("function", self.function)
        self.type = dict_model.get("type", self.type)
        self.status = dict_model.get("status", self.status)

        return self
    
    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
