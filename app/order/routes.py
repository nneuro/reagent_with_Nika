from app import app, db
from flask import redirect, render_template, url_for, flash, request
from app.order.models import ItemInOrder
from app.order.forms import ReagentOrderForm
from flask_login import current_user, login_required
from datetime import datetime


@app.route('/reagent_get', methods=['GET', 'POST'])
@login_required
def reagent_get():
    form = ReagentOrderForm()
    if form.validate_on_submit():
        reagent = ItemInOrder(author=current_user,
                              reagent_name=form.reagent_name.data, package=form.package.data,
                              package_unit=form.package_unit.data, vendor_name=form.vendor_name.data,
                              catalogue_number=form.catalogue_number.data, url_reagent=form.url_reagent.data,
                              urgency=form.urgency.data, reagent_comments=form.reagent_comments.data,
                              reagent_aim=form.reagent_aim.data)
        db.session.add(reagent)
        db.session.commit()
        flash('Реактив добавлен в Заказ')
        return redirect(url_for('reagent_get'))

    return render_template('reagent_get.html', title='Добавление нового реактива', form=form)


@app.route('/reagent_list')
def reagent_list():
    
    # items = ItemInOrder.query.all()
    items = []
    reagent_list_1=ItemInOrder.query.all()
    for item in reagent_list_1:
        form = ReagentOrderForm()
        if form.validate_on_submit():
            
            reagent = ItemInOrder.query.get(id)
            reagent.reagent_status = 'Новый заказ'
            db.session.commit()
            flash('Реактив добавлен в Новый заказ')

        items.append(item)
    return render_template('reagent_list.html', items=items, form=form)



@app.route('/reagent_list_checkbox', methods=['GET', 'POST'])
def reagent_list_checkbox():
    
    items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
    if request.method == 'GET':
        items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
        return render_template('reagent_list_checkbox.html', items=items)
    elif request.method == 'POST' and form.validate_on_submit():
        return render_template('result-form.html', form=form)
    return render_template('reagent_list_checkbox.html', items=items)



from app.order.forms import Reagent_checkbox, MultiCheckboxField
from flask_wtf import FlaskForm
from wtforms import SubmitField
@app.route('/reagent_checkbox_field_', methods=['GET', 'POST'])
def reagent_checkbox_field_():
    
    items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
    blank_list=[]
    for i in items:
        c=f'{i.reagent_name}, {i.package}, {i.package_unit}, {i.vendor_name}'
        blank_list.append(
            (i.id, i)
        )
    choices = blank_list
    # print(choices)
    #class Reagent_checkbox(FlaskForm):
    #    choices = blank_list
    #    reagent_checkbox_field = MultiCheckboxField('Выбранные реактивы',choices=choices, coerce=int)
        
    form = Reagent_checkbox()
    form.reagent_checkbox_field.choices = blank_list

    if request.method == 'GET':
        print(form.reagent_checkbox_field)
        # print(form.reagent_checkbox_field, dir(form.reagent_checkbox_field))
        return render_template('reagent_checkbox_field_.html', form=form, items=items)

    if request.method == 'POST':# and form.validate_on_submit():
        # print(form)
        # print(form, dir(form))
        # print(form.field.label)
        if '_send' in request.form:
            print(11111)
        return render_template('result-form1.html',
                           form=form, items=items)
    return render_template('reagent_checkbox_field_.html',
                         form=form, items=items)                        









# from app.order.forms import MultiCheckboxField
# @app.route('/reagent_list_checkbox_2', methods=['GET', 'POST'])
# def reagent_list_checkbox_2():
          
#     items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
          
#     blank_list=[]
#     for i in items:
#         a=i.id
#         b=(int(a))
#         c=str(a)
#         d=(b, c)
#         blank_list.append(d)
#     choices = blank_list
#     print(choices)
       
#     resident = MultiCheckboxField('Label',choices=choices, coerce=int)
#     return render_template('reagent_list_checkbox_2.html', items=items, choices=choices, resident=resident)                         


# @app.route('/reagent_list_checkbox_1', methods=['GET', 'POST'])
# def reagent_list_checkbox_1():
    
    
    
#     items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
    
#     return render_template('reagent_list_checkbox_1.html', items=items)

    # if request.method == 'POST':
    # elif request.method == 'GET':
        
    #     items = ItemInOrder.query.all()

    #     return render_template('result-form.html',items=items)
    # return render_template('reagent_list_checkbox_1.html',items=items)



# @app.route('/reagent_list_checkbox', methods=['GET', 'POST'])
# def reagent_list_checkbox():
#     if request.method == 'GET':
#         items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
#         return render_template('reagent_list_checkbox.html', items=items)
#     elif request.method == 'POST':
#         items2 = form.



    


