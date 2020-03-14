from .. import db
import datetime


class Link(db.Model):
    __tablename__ = "link"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(2048), unique=True, nullable=False)
    longhash = db.Column(db.String(256), unique=True, nullable=False)
    shorthash = db.Column(db.String(9), unique=True, nullable=False)

    def __repr__(self):
        return "<Link '{}'>".format(self.url)

