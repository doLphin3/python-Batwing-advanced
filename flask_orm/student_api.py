import http

import sqlalchemy.exc
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import school_db
from models.school import Student
from serializers.student import StudentSchema

student_router = Blueprint('student', __name__, url_prefix='/student')


@student_router.route('')
def get():
    student_schema = StudentSchema()

    students = Student.query.order_by(Student.id)
    students_json = student_schema.dump(students, many=True)
    return jsonify(students_json)


@student_router.route('/<int:id_>')
def retrieve(id_):
    student_schema = StudentSchema()
    student = Student.query.filter_by(id=id_).first()
    student_json = student_schema.dump(student)
    return jsonify(student_json)


@student_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)
    schema = StudentSchema()

    try:
        student_data = schema.load(data)
        try:
            new_student = Student(name=student_data['name'])
            school_db.session.add(new_student)
            school_db.session.commit()
            new_student_json = schema.dump(new_student)
        except sqlalchemy.exc.IntegrityError:
            return "Student already exists", http.HTTPStatus.BAD_REQUEST

    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_student_json


@student_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = StudentSchema()
    try:
        student_data = schema.load(data)
        student = Student.query.filter_by(id=id_).first()
        student.name = student_data['name']
        school_db.session.add(student)
        school_db.session.commit()

        new_student_json = schema.dump(student)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_student_json


@student_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Student.query.filter_by(id=id_).delete()
    school_db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
