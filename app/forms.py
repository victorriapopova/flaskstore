from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, URL, NumberRange, Length


class AddHeadphoneForm(FlaskForm):
    name = StringField('Наименование', validators=[DataRequired(), Length(max=100)])
    description = StringField('Описание', validators=[DataRequired(), Length(max=255)])
    price = FloatField('Цена (руб)', validators=[DataRequired(), NumberRange(min=0)])
    image_url = StringField('URL изображения', validators=[DataRequired(), URL()])
    submit = SubmitField('Добавить наушники')
