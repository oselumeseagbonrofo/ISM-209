# import flask
from flask import Flask, render_template

# initialise flask app
app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/hobbies")
def hobbies_page():
    return render_template("hobbies.html")


@app.route("/projects")
def projects_page():
    return render_template("projects.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
