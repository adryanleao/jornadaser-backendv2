import uuid
from app import db

from app.models.base import BaseModel


class ExtraMaterial(db.Model, BaseModel):
    __tablename__ = "extra_material"

    hash_id = db.Column(db.String(36), unique=True, nullable=False, default=lambda x: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(255))
    user_type = db.Column(db.String(255))
    module = db.Column(db.String(255))
    link = db.Column(db.String(255))
    file_key = db.Column(db.String(255))
    status = db.Column(db.Boolean(), nullable=False, default=1)
    
    
    school_class_id = db.Column(db.Integer, db.ForeignKey('school_class.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
    
    category = db.relationship('Category', uselist=False, backref="extra_material")
    school_class = db.relationship('SchoolClass', uselist=False, backref="extra_material")
    institution = db.relationship('Institution', uselist=False, backref="extra_material")


    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
