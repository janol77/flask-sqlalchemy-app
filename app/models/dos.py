from datetime import datetime
from db import db


class Dos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)
    uno_id = db.Column(db.Integer, db.ForeignKey('uno.id'))

    def __repr__(self):
        return '<Dos %r>' % self.title
