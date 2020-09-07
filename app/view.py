from json import dumps
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
    if request.method == "GET":
        return render_template("index.html", form=form, sentence=sentence)
    elif (
        request.method == "POST"
    ):  # INSERT managment empty query (Random sentence from GranPy for empty queries)
        infos = get_infos(request.json["sentence"])
        infos_into_JSON = turn_into_JSON(*infos)
        return infos_into_JSON, 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


def get_infos(sentence):
    """Parse an input sentence and try to get infos from it, coordinates,
    extract from Wikipedia and url."""

    parser = Parser(sentence)
    location = Location(parser)

    try:
        location.get_location()
    except UnknownPlaceError:  # INSERT random system for unknown location
        return "Je suis désolé, je n'ai pas bien compris. Peux-tu répéter ?"

    story = Story(location)
    story.about()
    return location.latitude, location.longitude, story.extract, story.url


def turn_into_JSON(latitude, longitude, extract, url):
    """Turn coordinates of place and wikipedia informations into JSON data."""

    infos = {
        "latitude": latitude,
        "longitude": longitude,
        "extract": extract,
        "url": url,
        "apiKey": environ.get("GOOGLE_KEY"),
    }

    return dumps(infos)
