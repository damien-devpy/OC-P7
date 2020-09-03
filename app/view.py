from os import environ

from app.location import Location
from app.parser import Parser
from app.questionform import QuestionForm
from app.story import Story
from app.unknownplaceerror import UnknownPlaceError
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = environ.get("SECRET_KEY_FLASK")


@app.route("/", methods=["GET", "POST"])
def index():
    sentence = None
    form = QuestionForm()
    if request.method == "POST":
        sentence = parsing_input_user(request.json["input"])
    return render_template("index.html", form=form, sentence=sentence)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


def parsing_input_user(sentence):

    parser = Parser(sentence)
    location = Location(parser)

    try:
        location.get_location()
    except UnknownPlaceError:
        return "Je suis désolé, je n'ai pas bien compris. Peux-tu répéter ?"

    story = Story(location)
    story.about()
    return location.latitude, location.longitude, story.extract, story.url
