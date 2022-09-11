from main import db, school_db
from models.user import User
from models.school import Student

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(User(email="andrii@gmail.com"))
    db.session.commit()

    school_db.create_all()
    school_db.session.commit()

    print("created tables")
