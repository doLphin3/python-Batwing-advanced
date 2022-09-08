from flask import Flask
import http

from user_api import user_router
from book_api import book_router

app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(book_router)

status_code_created = 201


@app.route('/')
def index():
    return "hello world"


@app.route("/<bad_request>")
def bad_request(bad_request):
    return "We cannot found the requested resource. Try '/user' or '/book'", http.HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(debug=True)
