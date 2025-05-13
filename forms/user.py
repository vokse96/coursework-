from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    tel = StringField('Введите телефон', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class ConfirmationForm(FlaskForm):
    code = StringField('Введите код подтверждения', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')

