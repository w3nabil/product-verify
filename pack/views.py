"""
This module contains the public visible routes of the application,
and handling several reguest methods.

Author: NABIL 
Date: 29/03/2024
"""

from flask import render_template, Blueprint, request , redirect, url_for
from . import db
from .sqlite import Product
from .models import check_query, check_pass

views = Blueprint('views', __name__, template_folder='public', static_folder='src')

@views.route('/')
# Home page
def home():
    return render_template('index.html')

@views.route('/add', methods=['GET', 'POST'])
# Add product page
def add():
    if request.method == 'POST':
        name = request.form['name']
        product_id = request.form['id'].upper()
        price = request.form['price']
        manufacturer = request.form['manufacturer']
        manufacture_date = request.form['manufacture_date']
        expiry_date = request.form['expiry_date']
        batch_number = request.form['batch_number']
        key = request.form['key'].upper()

        new_product = Product(
            name=name,
            product_id=product_id,
            price=price,
            manufacturer=manufacturer,
            manufacture_date=manufacture_date,
            expiry_date=expiry_date,
            batch_number=batch_number,
            key=key
            )

        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('views.add'))
    return render_template('register.html')

@views.route('/verify', methods=['GET', 'POST'])
# Verify product page
def verify():
    if request.method == 'POST':
        product_id = request.form['product_id'].upper()
        message = None
        error_search = check_query(product_id)
        if error_search is None:
            key = request.form['key'].upper()
            product = Product.query.filter_by(product_id=product_id).first()
            error = check_pass(key)
            if error is None:
                if product:
                    if product.key == key:
                        return render_template('verify.html', product=product, message=message)
                    message = 'Invalid key'
                    return render_template('verify.html', message=message)
                message = 'Invalid product id'
                return render_template('verify.html', message=message)
            message = error
            return render_template('verify.html', message=message)
        message = error_search
        return render_template('verify.html', message=message)
    return redirect(url_for('views.home'))

