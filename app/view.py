from flask import Flask, render_template
from app.questionform import QuestionForm
from app.parser import Parser
from app.googleapi import GoogleAPI
from app.unknownplaceerror import UnknownPlaceError
from os import environ

app = Flask(__name__)
app.config["SECRET_KEY"] = environ.get("SECRET_KEY_FLASK")


@app.route("/", methods=["GET", "POST"])
def index():
    sentence = None
    form = QuestionForm()
    if form.validate_on_submit():
        sentence = parsing_input_user(form.name.data)
    return render_template("index.html", form=form, sentence=sentence,)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


def parsing_input_user(sentence):

    parser = Parser()
    parser.input_user = sentence

    api_google = GoogleAPI(parser)

    try:
        current_location = api_google.location
    except UnknownPlaceError as err:
        return "Je suis désolé, je n'ai pas bien compris. Peux-tu répéter ?"

    return current_location, parser.parse()
