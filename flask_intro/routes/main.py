from app import app
from flask import render_template


@app.route("/")
def hello_world():
    return render_template("index.html", var="Gigity")


@app.route("/add/<first>/<second>")
def adding(first, second):
    sum = int(first) + int(second)
    return render_template("index.html", var=sum)
