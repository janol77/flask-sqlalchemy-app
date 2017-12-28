from datetime import datetime
from db import db


class Uno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    doses = db.relationship(
        'Dos',
        backref=db.backref('uno', lazy=True))

    def __repr__(self):
        return '<Uno %r>' % self.title