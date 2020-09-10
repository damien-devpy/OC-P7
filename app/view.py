from json import dumps
from os import environ
from random import sample

from app.configuration import (INFOS, RANDOM_SENTENCE_ERROR,
                               RANDOM_SENTENCE_GRANPY,
                               RANDOM_SENTENCE_UNKWON_PLACE)
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
    elif request.method == "POST":
        # If incoming request object contains existing JSON data
        if bool(request.is_json and request.json["sentence"].strip()):
            infos, error = get_infos(request.json["sentence"])
            infos_into_JSON = turn_into_JSON(*infos, request_ok=error)
            return infos_into_JSON, 200
        else:
            # Else returning random error message look like coming from GranPy
            error_message = turn_into_JSON(
                sample(RANDOM_SENTENCE_ERROR, 1), request_ok=False
            )
            return error_message, 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


def get_infos(sentence):
    """Parse an input sentence and try to get infos from it, coordinates,
    extract from Wikipedia and url.

    Args:

        sentence (string): Sentence from user input

    Returns:

        tuple: Informations gathered from input parsed (coordinates, url to
            wikipedia, random message from GranPy)

        boolean: Does the parsing and finding informations occured normally

    """

    parser = Parser(sentence)
    location = Location(parser)

    try:
        location.get_location()
        story = Story(location)
        story.about()
    except UnknownPlaceError:
        # If Harold doesn't found requested location, returning random sentence
        # of error
        return sample(RANDOM_SENTENCE_UNKWON_PLACE, 1), False

    return (
        sample(RANDOM_SENTENCE_GRANPY, 1),
        location.latitude,
        location.longitude,
        story.extract,
        story.url,
    ), True


def turn_into_JSON(*args, request_ok):
    """Turn coordinates of place and wikipedia informations into JSON data.

    Args:

        *args (tuple): Multiple args (error, message, latitude, longitude, ...)
        request_ok (boolean): Does parsing and finding location turn out ok.

    Return:

        INFOS (json): Dict turn into JSON data"""

    if request_ok:
        INFOS["error"] = "false"
        INFOS["message"] = args[0]
        INFOS["latitude"] = args[1]
        INFOS["longitude"] = args[2]
        INFOS["extract"] = args[3]
        INFOS["url"] = args[4]
        INFOS["apiKey"] = environ.get("GOOGLE_KEY")
    else:
        INFOS["error"] = "true"
        INFOS["message"] = args[0]

    return dumps(INFOS)
