from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

# class RegisterForm(FlaskForm):
#     email = StringField('login/email', validators=[DataRequired()])
#     fpassword = PasswordField('Password', validators=[DataRequired()])
#     spassword = PasswordField('Repeat password', validators=[DataRequired()])
#
#     surname = StringField('surname', validators=[DataRequired()])
#     name = StringField('name', validators=[DataRequired()])
#     age = StringField('age', validators=[DataRequired()])
#     position = StringField('position', validators=[DataRequired()])
#     speciality = StringField('speciality', validators=[DataRequired()])
#     address = StringField('address', validators=[DataRequired()])
#     submit = SubmitField('Доступ')
#
#
# class LoadForm(FlaskForm):
#     fileName = FileField()
#
#
# class TwoLogin(FlaskForm):
#     fid = StringField('id астронафта', validators=[DataRequired()])
#     fpassword = PasswordField('Пароль астронафта', validators=[DataRequired()])
#     sid = StringField('id капитана', validators=[DataRequired()])
#     spassword = PasswordField('Пароль капитана', validators=[DataRequired()])
#     submit = SubmitField('Доступ')
