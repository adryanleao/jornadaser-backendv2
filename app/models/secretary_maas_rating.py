from app import db
from app.models.base import BaseModel


class SecretaryMaasRating(db.Model, BaseModel):
    __tablename__ = "secretary_maas_rating"

    rating = db.Column(db.Integer)
    maas_id = db.Column(db.Integer, db.ForeignKey('maas.id'))
    secretary_id = db.Column(
        db.Integer, db.ForeignKey('secretary.id'))
    
    maas = db.relationship("Maas", uselist=False, backref="secretary_maas_rating")

    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
