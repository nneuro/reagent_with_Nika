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


from flask import Flask, render_template, request
from app.order.forms import BrifStoreForm

@app.route('/brif-store', methods=['GET', 'POST'])
def brif_store():
    form = BrifStoreForm()
    if request.method == 'GET':
        print(form.resident, dir(form.resident))
        return render_template('brif-store.html', form=form)
    print(form.choices)
    if request.method == 'POST':# and form.validate_on_submit():
        print(form, dir(form))
        return render_template('result-form1.html',
                           form=form)
    return render_template('brif-store.html',
                         form=form)


from app.order.forms import BrifStoreForm1
from flask_wtf import FlaskForm
from wtforms import SubmitField
@app.route('/brif-store1', methods=['GET', 'POST'])
def brif_store1():
    
    items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
    blank_list=[]
    for i in items:
        a=i.id
        b=(int(a))
        c=f'{i.reagent_name}, {i.vendor_name}, {i.package}, {i.package_unit}'
        d=(b, c)
        blank_list.append(d)
    choices = blank_list
    print(choices)
    class BrifStoreForm1(FlaskForm):
        choices = blank_list
        resident = MultiCheckboxField('Выбранные реактивы',choices=choices, coerce=int)
        submit = SubmitField('тест submit', render_kw={"class": "form-check-label"})

    form = BrifStoreForm1()

    if request.method == 'GET':
        print(form.resident, dir(form.resident))
        return render_template('brif-store1.html', form=form)

    if request.method == 'POST':# and form.validate_on_submit():
        print(form, dir(form))
        return render_template('result-form1.html',
                           form=form)
    return render_template('brif-store1.html',
                         form=form)                        



from app.order.forms import MultiCheckboxField
@app.route('/reagent_list_checkbox_2', methods=['GET', 'POST'])
def reagent_list_checkbox_2():
      
    
    items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
    
       
    blank_list=[]
    for i in items:
        a=i.id
        b=(int(a))
        c=str(a)
        d=(b, c)
        blank_list.append(d)
    choices = blank_list
    print(choices)
    
    
    resident = MultiCheckboxField('Label',choices=choices, coerce=int)
    return render_template('reagent_list_checkbox_2.html', items=items, choices=choices, resident=resident)                         


@app.route('/reagent_list_checkbox_1', methods=['GET', 'POST'])
def reagent_list_checkbox_1():
    
    
    
    items = ItemInOrder.query.filter_by(reagent_status='черновик').order_by(ItemInOrder.vendor_name).all()
    
    return render_template('reagent_list_checkbox_1.html', items=items)

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



    


