from database import school_db


class Student(school_db.Model):
    __tablename__ = 'students'

    id = school_db.Column(school_db.Integer, primary_key=True, autoincrement=True)
    name = school_db.Column(school_db.String(300), nullable=False, unique=True)
