from flask import Flask, render_template
from app.questionform import QuestionForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "temporary secret in my code :o)"


@app.route("/", methods=["GET", "POST"])
def index():
    question = None
    form = QuestionForm()
    if form.validate_on_submit():
        question = form.name.data
    return render_template("index.html", form=form, question=question)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
