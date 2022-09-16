from database import db


class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
