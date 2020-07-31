from flask import Flask, render_template
from app.questionform import QuestionForm
from app.parser import Parser

app = Flask(__name__)
app.config["SECRET_KEY"] = "temporary secret in my code :o)"


@app.route("/", methods=["GET", "POST"])
def index():
    sentence = None
    form = QuestionForm()
    if form.validate_on_submit():
        sentence = parsing_input_user(form.name.data)
    return render_template("index.html", form=form, sentence=sentence)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


def parsing_input_user(sentence):

    parser = Parser()
    parser.input_user = sentence

    return parser.parse()
