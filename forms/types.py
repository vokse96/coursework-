from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TypeForm(FlaskForm):
    title = StringField('Название типа', validators=[DataRequired()])
    submit = SubmitField('Добавить')
