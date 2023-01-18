from app import db, models
from app.models.base import BaseModel


class Team(db.Model, BaseModel):
    __tablename__ = "team"

    name = db.Column(db.String(255))
    module = db.Column(db.String(255))
    status = db.Column(db.Boolean(), nullable=False, default=1)
    
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'))
    
    teacher = db.relationship('User', backref='teacher', lazy=True, uselist=False, foreign_keys=[teacher_id])
    institution = db.relationship('Institution', backref='team', lazy=True, uselist=False)

    def _get_students(self):
        return models.User.query.filter(
            models.User.team_id == self.id,
            models.User.group_id == 6,
            models.User.deleted_at.is_(None)
        ).all()

    students = property(_get_students)
    
    def __init__(self, **kwargs):
        allowed_args = self.__mapper__.class_manager  # returns a dict
        kwargs = {k: v for k, v in kwargs.items() if k in allowed_args}
        super().__init__(**kwargs)
