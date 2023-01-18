from app import db
from app.models.base import BaseModel


class MainCompany(db.Model, BaseModel):
    __tablename__ = "main_company"

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    cell_phone = db.Column(db.String(256), nullable=False)
    landline = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=1)

    # company
    ein = db.Column(db.String(256))
    company_name = db.Column(db.String(256))

    # social
    facebook = db.Column(db.String(256))
    instagram = db.Column(db.String(256))

    # app
    app_android = db.Column(db.String(256))
    app_ios = db.Column(db.String(256))

    address = db.relationship("MainCompanyAddress", uselist=False,
                              backref="company")
