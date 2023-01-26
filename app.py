from flask import Flask, request, render_template, redirect, url_for
from csv import DictReader, DictWriter

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == 'GET':
        return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)