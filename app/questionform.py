from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class QuestionForm(FlaskForm):
    """Create a form for user inputs."""

    name = StringField("")
    submit = SubmitField("Submit")
