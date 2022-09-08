import http
from flask import Blueprint, Response, request
from db.books_db import BookDB

book_router = Blueprint('book', __name__, url_prefix='/book')
db = BookDB()


@book_router.route('')
def get():
    books = db.get_all()
    return Response(str(books))


@book_router.route('/<string:name>')
def retrieve(name):
    book = db.retrieve_by_name(name)
    return book


@book_router.route('', methods=['POST'])
def create():
    name = request.json.get("name")
    author = request.json.get("author")
    new_book = db.add(name, author)
    if new_book:
        return new_book, http.HTTPStatus.CREATED
    else:
        return "Book already exists", http.HTTPStatus.BAD_REQUEST


@book_router.route('/<string:name>', methods=['DELETE'])
def delete(name):
    db.delete_by_name(name)
    return {}, http.HTTPStatus.NO_CONTENT
