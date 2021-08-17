from typing import Coroutine
from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from sqlalchemy.orm import query
from sqlalchemy.sql.sqltypes import String
from model import db, app, instructorlogin, needed
from model import course,instructor,enrolls,needed,customerlogin,customer,product,cart

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import cast

@app.route("/")
def home():
    return render_template('login.html')

@app.route('/customer_login')
def customer_login():
    return render_template('customer_login.html')

@app.route('/instructor_login')
def instructor_login():
    return render_template('instructor_login.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/instructor_page_checkin', methods=['GET', 'POST'])
def instructor_page_checkin():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

            instlog = instructorlogin.query.filter_by(instructorlogin_user = username, instructorlogin_pass = password).first()
            if instlog:  # if a user is found, we want to redirect back to signup page so user can try again
                inst = instructor.query.filter_by(inst_id=instlog.instructorlogin_id).first()
                print(inst.inst_fname)
                print(instlog.instructorlogin_id)
                courses = course.query.filter_by(course_inst_id=inst.inst_id).all()
                response = make_response(render_template('instructor_page.html', instructor_info = inst, courses_by_instructor = courses))
                response.set_cookie("inst_id", str(inst.inst_id))

                return response

            else:
                return render_template('instructor_login.html')

    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page




@app.route('/instructor_page', methods=['GET', 'POST'])
def instructor_page():
    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page
    id = request.args.get('id')
    value= request.args.get('value')
    print(request.cookies.get('inst_id'))
    instid = request.cookies.get('inst_id',type=int)
    if id == 'deletebutton':
        course_toBeDeleted = course.query.filter_by(course_id = value).first()
        needed.query.filter_by(needed_course_id = value).delete()
        enrolls.query.filter_by(enrolls_course_id = value).delete()
        db.session.delete(course_toBeDeleted)
        db.session.commit()
        inst = instructor.query.filter_by(inst_id=instid).first()
        courses = course.query.filter_by(course_inst_id=instid).all()
        response = make_response(render_template('instructor_page.html',instructor_info=inst,courses_by_instructor=courses))
    if id == 'editbutton':
        inst = instructor.query.filter_by(inst_id=instid).first()
        course_toBeEdited = course.query.filter_by(course_id = value).first()
        print(course_toBeEdited.course_name)
        response = make_response(render_template('instructor_edit.html',instructor_info=inst,selected_course=course_toBeEdited))  
        response.set_cookie("course_id", str(course_toBeEdited.course_id))      
    
    

    return response


@app.route('/instructor_edit', methods=['GET', 'POST'])
def instructor_edit():
    instid = request.cookies.get('inst_id',type=int)
    coursesid = request.cookies.get('course_id',type=int)
    inst = instructor.query.filter_by(inst_id=instid).first()   
    course_toBeEdited = course.query.filter_by(course_id = coursesid).first()
    if request.method == 'POST':
             course_toBeEdited.course_name= request.form.get('Name')
             course_toBeEdited.course_category = request.form.get('Category')
             course_toBeEdited.course_level = request.form.get('Level')
             course_toBeEdited.course_price = request.form.get('Price')
             course_toBeEdited.course_duration = request.form.get('Duration')
             db.session.commit()

             courses = course.query.filter_by(course_inst_id=instid).all()

             response = make_response(render_template('instructor_page.html',instructor_info=inst,courses_by_instructor=courses))
             return response

@app.route('/customer_page_checkin', methods=['GET', 'POST'])
def customer_page_checkin():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            return render_template('instructor_login.html')
        else:
            username = request.form.get('username')
            password = request.form.get('password')
        custlog = customerlogin.query.filter_by(customerlogin_user = username, customerlogin_pass = password).first()
        if custlog:  # if a user is found, we want to redirect back to signup page so user can try again
            cust = customer.query.filter_by(cust_id=custlog.customerlogin_id).first()
            response = make_response(render_template('customer_page.html',customer_info=cust))
            response.set_cookie("cust_id", str(cust.cust_id))

            return response

        else:
            return render_template('instructor_login.html')


@app.route('/customer_page', methods=['GET', 'POST'])
def customer_page():
    custlogid = request.cookies.get('cust_id',type=int)
    customer_info =customer.query.filter_by(cust_id = custlogid).first()
    return render_template('customer_page.html',customer_info=customer_info)

@app.route('/all_courses', methods=['GET', 'POST'])
def all_courses():

    if request.method == 'POST':
            if(request.form.get('CourseID') != ''):
                searched_course = request.form.get('CourseID')
                searched_course_tag1 = "%{}%".format(searched_course)
                filtered_courses = course.query.filter_by(course_id = searched_course)
            elif(request.form.get('InstructorID') != ''):
                searched_course = request.form.get('InstructorID')
                searched_course_tag1 = "%{}%".format(searched_course)
                filtered_courses = course.query.filter_by(course_inst_id = searched_course)

            elif(request.form.get('Name') != ''):
                searched_course = request.form.get('Name')
                searched_course_tag1 = "%{}%".format(searched_course)
                filtered_courses = course.query.filter(course.course_name.ilike(searched_course_tag1))

            elif(request.form.get('Category') != ''):
                searched_course = request.form.get('Category')
                searched_course_tag1 = "%{}%".format(searched_course)
                filtered_courses = course.query.filter(course.course_name.ilike(searched_course_tag1))
            elif(request.form.get('Level') != ''):
                searched_course = request.form.get('Level')
                searched_course_tag1 = "%{}%".format(searched_course)
                filtered_courses = course.query.filter_by(course_level = searched_course)
            elif(request.form.get('Duration') != ''):
                searched_course = request.form.get('Duration')
                searched_course_tag1 = "%{}%".format(searched_course)
                filtered_courses = course.query.filter_by(course_duration = searched_course)
            else:
                filtered_courses = course.query.all()
        
            return render_template('all_courses.html', all_courses=filtered_courses)

    all_courses = course.query.all()

    id = request.args.get('id') #==show_related ise
    value = request.args.get('value') #
    if id=='show_related':

        selected_course = course.query.filter_by(course_id = value).first()
        need = needed.query.filter_by(needed_course_id = value).all()
        list = []
        for x in need:
            list.append(product.query.filter_by(prod_id = x.needed_prod_id).first())
        return render_template('all_courses_related_product.html',selected_course=selected_course,related_products=list)

    return render_template('all_courses.html',all_courses=all_courses)

@app.route('/all_courses_related_product', methods=['GET', 'POST'])
def all_courses_related_product():
    return render_template('all_courses_related_product.html')

        
@app.route('/all_products', methods=['GET', 'POST'])
def all_products():
    id = request.args.get('id') #==add_to_Cart ise
    value = int(request.args.get('value')) #product id
    products2 = [{
        'prod_id': '111111',
        'prod_name': 'bahcivan',
        'prod_brand': 'bahçe',
        'prod_weight': '5',
        'prod_price': '120',
        'prod_instock': '122'}, {
        'prod_id': '22222',
        'prod_name': 'bahcivan',
        'prod_brand': 'bahçe',
        'prod_weight': '5',
        'prod_price': '120',
        'prod_instock': '122'}, {
        'prod_id': '333333',
        'prod_name': 'bahcivan',
        'prod_brand': 'bahçe',
        'prod_weight': '5',
        'prod_price': '120',
        'prod_instock': '122'}]
    products = product.query.filter_by().all()
    if id=='add_to_cart':
        added_product= product.query.filter_by(prod_id=value).first()
       # new_cart = cart(cart_cust_id=,cart_prod_id=,cart_prodcount=1)
        #db.session.add(new_cart)
        #db.session.commit()
        print(products)
        print(added_product)
        #add selected product to cart

    return render_template('all_products.html',products=products)

@app.route('/cart', methods=['GET', 'POST'])
def carts():
    custid = request.cookies.get('cust_id',type=int)
    id = request.args.get('id') #==delete_from_cart ise
    value = request.args.get('value') #product id
    products_in_cart= cart.query.filter_by(cart_cust_id = custid)
    if id=='delete_from_cart':
        selected_product = cart.query.filter_by(cart_cust_id = custid, cart_prod_id = value)
        db.session.delete(selected_product)
        db.session.commit()
    if id=='add_to_order':
        #add products in cart to order data table
        #empty cart
        print(id)

    return render_template('cart.html',products=products_in_cart)


@app.route('/my_courses', methods=['GET', 'POST'])
def my_courses():
    my_all_courses= [{
        'course_id': '111111',
        'course_name': 'bahcivan',
        'course_category': 'bahçe',
        'course_level': '5',
        'course_price': '120',
        'course_duration': '122',
         'course_inst_id': '122'}]

    return render_template('my_courses.html',courses=my_all_courses)


@app.route('/order', methods=['GET', 'POST'])
def order():
    products_in_order= [{
        'prod_id': '111111',
        'prod_name': 'bahcivan',
        'prod_brand': 'bahçe',
        'prod_weight': '5',
        'prod_price': '120',
        'prod_instock': '122'}, {
        'prod_id': '22222',
        'prod_name': 'bahcivan',
        'prod_brand': 'bahçe',
        'prod_weight': '5',
        'prod_price': '120',
        'prod_instock': '122'}, {
        'prod_id': '333333',
        'prod_name': 'bahcivan',
        'prod_brand': 'bahçe',
        'prod_weight': '5',
        'prod_price': '120',
        'prod_instock': '122'}]

    return render_template('order.html',products=products_in_order)


@app.route('/admin_page', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page

    return render_template('admin_page.html')