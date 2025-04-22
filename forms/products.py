from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, MultipleFileField, widgets, SelectMultipleField
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class ProductForm(FlaskForm):
    title = StringField('Название продукта', validators=[DataRequired()])
    description = StringField('Описание продукта', validators=[DataRequired()])
    type = SelectField('Тип продукта', coerce=int, choices=[(0, '0')])
    cost = StringField("Стоимость в рублях", validators=[DataRequired()])
    sale = StringField('Наличие скидки на старте (Скидка в %)', validators=[DataRequired()], default='0')
    special_offer = StringField("Спецальное предложение на старте (Скидка в %)", validators=[DataRequired()],
                                default='0')
    img = MultipleFileField(validators=[])
    imgs = MultiCheckboxField('Label', choices=[(1, '1'), (2, '2')])

    submit = SubmitField('Подтвердить')

    def __init__(self, *args, data=[(1, '1')], imgs_data=[], must_upload=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.type.choices = data
        self.imgs.choices = imgs_data
        if not must_upload:
            self.img.validators = []

# class ChangeProductForm(FlaskForm):
#     title = StringField('Название продукта', validators=[DataRequired()])
#     description = StringField('Описание продукта', validators=[DataRequired()])
#     type = SelectField('Тип продукта', coerce=str, choices=[(0, '0')])
#     cost = StringField("Стоимость в рублях", validators=[DataRequired()])
#     sale = StringField('Наличие скидки на старте (Скидка в %)', validators=[DataRequired()], default='0')
#     special_offer = StringField("Спецальное предложение на старте (Скидка в %)", validators=[DataRequired()],
#                                 default='0')
#     photos =
#
#     img = MultipleFileField(validators=[DataRequired('No selected file')])
#
#     submit = SubmitField('Подтвердить')
#
#     def __init__(self, *args, data=[(1, '1')], photo_data=[], must_upload=True, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.type.choices = data
#         if not must_upload:
#             self.img.validators=[]
#
