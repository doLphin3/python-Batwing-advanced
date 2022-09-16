import http
from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from database import db
from models.author import Author
from models.book import Book
from serializers.book import BookSchema

book_router = Blueprint('book', __name__, url_prefix='/book')


@book_router.route('')
def get():
    book_schema = BookSchema()
    books = Book.query.order_by(Book.id)
    books_json = book_schema.dump(books, many=True)
    return jsonify(books_json)


@book_router.route('/<int:id_>')
def retrieve(id_):
    book_schema = BookSchema()
    book = Book.query.filter_by(id=id_).first()
    book_json = book_schema.dump(book)
    return jsonify(book_json)


@book_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)
    schema = BookSchema()

    try:
        book_data = schema.load(data)
        new_book = Book(name=book_data['name'], description=book_data['description'])
        db.session.add(new_book)
        db.session.commit()
        new_book_json = schema.dump(new_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)
    schema = BookSchema()
    try:
        book_data = schema.load(data)
        book = Book.query.filter_by(id=id_).first()
        book.name = book_data['name']
        book.description = book_data['description']
        db.session.add(book)
        db.session.commit()
        new_book_json = schema.dump(book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Book.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT


@book_router.route('/<int:id_>/add_author/<int:author_id>', methods=['POST'])
def add_to_author(id_, author_id):
    book = Book.query.filter_by(id=id_).first()
    if author := Author.query.filter_by(id=author_id).first():
        book.author_id = author.id
        db.session.add(book)
        db.session.commit()
        schema = BookSchema()
        new_book_json = schema.dump(book)
        return new_book_json, http.HTTPStatus.OK
    else:
        return {"No author found"}, http.HTTPStatus.BAD_REQUEST
