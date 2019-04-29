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
    
    items = ItemInOrder.query.order_by(ItemInOrder.vendor_name).all()
    blank_list=[]
    for i in items:
        blank_list.append((i.id, i))
            
    form = Reagent_checkbox()
    form.reagent_checkbox_field.choices = blank_list

    if request.method == 'GET':
        return render_template('reagent_checkbox_field_.html', form=form, items=items)

    if request.method == 'POST':
        if '_send' in request.form:
            return render_template('result-form1.html',
                           form=form, items=items)
       
    return render_template('reagent_checkbox_field_.html',
                         form=form, items=items)         

@app.route('/calc_start', methods=['GET', 'POST'])
def calc_start():
    if request.method == 'GET':
        print('debug up')
        return render_template('calc_start.html')

    if request.method == 'POST':
        print('debug5')

        if '_calc_mass' in request.form: 
            print('debug calc start')
            return redirect(url_for('calc_mass'))
        elif '_calc_molar' in request.form: 
            return redirect(url_for('calc_molar'))

            

           
from app.order.forms import CalculatorForm

@app.route('/calc_mass', methods=['GET', 'POST'])
def calc_mass():
    form = CalculatorForm()
    
    if request.method == 'GET':
        return render_template('calc_mass.html', form=form)

    if request.method == 'POST':
        print('debug3')

        if '_calc' in request.form:
            print('debug4')
            print(form.molar_conc_unit.data)
            print(type(form.molar_conc_unit.data))
            
            coef_molar_conc =10**(int(form.molar_conc_unit.data)*(-1))
            coef_vol = 10**(int(form.vol_unit.data)*(-1))
            mass_1 = (float(form.molar_conc.data)*coef_molar_conc*coef_vol*float(form.volume.data)*float(form.molar_mass.data))
            
            if mass_1 >= 1:
                mass =  (f'Масса составляет {mass_1} грамм')
                return render_template('calc_result.html', mass=mass)
            elif 0.001<mass_1<1:
                mass = (f'Масса составляет {mass_1*1000} миллиграмм')
                return render_template('calc_result.html', mass=mass)
            elif 0.000001<mass_1<=0.001:
                mass = (f'Масса составляет {mass_1*1000000} микрограмм')
                return render_template('calc_result.html', mass=mass)
            elif mass_1<=0.000001:
                mass = (f'Масса составляет {mass_1*1000000000} нанограмм')
                return render_template('calc_result.html', mass=mass)
            

@app.route('/calc_molar', methods=['GET', 'POST'])
def calc_molar():
    form = CalculatorForm()
    
    if request.method == 'GET':
        return render_template('calc_molar.html', form=form)

    if request.method == 'POST':
        print('debug3')

        if '_calc' in request.form:
            print('debug4')
                        
            coef_mass = 10**(int(form.mass_unit.data)*(-1))
            coef_vol = 10**(int(form.vol_unit.data)*(-1))
            molar_conc_undef_1 = ((float(form.mass_def.data)*coef_mass)/(float(form.volume.data)*coef_vol*float(form.molar_mass.data)))
            
            if molar_conc_undef_1 >= 1:
                molar_conc_undef =  (f'Молярная концентрация составляет {molar_conc_undef_1} M')
                return render_template('calc_molar_result.html', molar_conc_undef=molar_conc_undef)
            elif 0.001<molar_conc_undef_1<1:
                molar_conc_undef = (f'Молярная концентрация составляет {molar_conc_undef_1*1000} mM')
                return render_template('calc_molar_result.html', molar_conc_undef=molar_conc_undef)
            elif 0.000001<molar_conc_undef_1<=0.001:
                molar_conc_undef = (f'Молярная концентрация составляет {molar_conc_undef_1*1000000} mkM')
                return render_template('calc_molar_result.html', molar_conc_undef=molar_conc_undef)
            elif molar_conc_undef_1<=0.000001:
                molar_conc_undef = (f'Молярная концентрация составляет {molar_conc_undef_1*1000000000} nM')
                return render_template('calc_molar_result.html', molar_conc_undef=molar_conc_undef)            
                

                
            

    


