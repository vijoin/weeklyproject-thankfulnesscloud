from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField


class RegisterThankful(FlaskForm):
    name = StringField()
    age = IntegerField()
    description = TextAreaField()
    submit = SubmitField()