from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField, TextAreaField, DecimalField
from wtforms import SelectMultipleField, widgets
from wtforms.validators import DataRequired, NumberRange
from app.order.constants import URGENCY, AIM


class ReagentOrderForm(FlaskForm):

    reagent_name = TextAreaField('* Название реактива', validators=[DataRequired()])

    package = StringField('* Фасовка, например: 500 грамм, 10 шт/уп, 100 мкг и т.п.', validators=[DataRequired()])
    package_unit = StringField('Единица измерения, например: шт, уп, набор и т.п.', validators=[DataRequired()])

    reagent_count = IntegerField('* Количество',
                                 validators=[DataRequired(), NumberRange(min=1)])

    vendor_name = StringField('* Название производителя', validators=[DataRequired()])

    catalogue_number = StringField('Каталожный номер или артикул')

    url_reagent = StringField('Ссылка на страницу реактива на сайте производителя')

    urgency = SelectField('Срочность заказа (стратегический означает, что можно заказать в течение полугода-года',
                          choices=URGENCY)
    reagent_aim = SelectField('Выберите или введите цель заказа реактива для служебной записки', choices=AIM)

    reagent_comments = TextAreaField('Комментарий к реактиву')

    submit = SubmitField('Добавить реактив в Заказ', render_kw={"class": "form-check-label"})

class ReagentToOrderForm(SelectMultipleField):
    option_widget = widgets.CheckboxInput()
    widget = widgets.ListWidget(prefix_label=False)
    
    

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class Reagent_checkbox(FlaskForm):
    choices = [(1, 'one'), (2, 'two'),]
    reagent_checkbox_field = MultiCheckboxField('Label',choices=choices, coerce=int)
    



class CalculatorForm(FlaskForm):
    molar_conc = DecimalField("Молярная концентрация")
    molar_conc_unit = SelectField('Единица молярной концентрации', choices = [
                    (0, 'M'),
                    (-3, 'mM'),
                    ((-6), 'mkM'),
                    ((-9), 'nM')])
    volume = DecimalField("Объём")
    vol_unit = SelectField('Единица объёма', choices = [
                    (0, 'L'),
                    (-3, 'ml'),
                    (-6, 'mkl'),
                    (-9, 'nl')])
    molar_mass = DecimalField("Молярная масса (грамм/моль)")
    mass_def = DecimalField("Масса")
    mass_unit = SelectField('Единица массы', choices = [
                    (0, 'g'),
                    (-3, 'mg'),
                    (-6, 'mkg'),
                    (-9, 'ng')])







    
