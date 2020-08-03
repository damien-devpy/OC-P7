from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    name = StringField(
        "Please ask me for a location", validators=[DataRequired()],
    )
    submit = SubmitField("Submit")
