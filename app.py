from datetime import date
from operator import add, ne
from typing import Coroutine
from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from sqlalchemy.orm import query
from sqlalchemy.sql.expression import null, text, update
from sqlalchemy.sql.sqltypes import DateTime, String
from model import db, app, instructorlogin, needed, orders, purchased

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
            return render_template('customer_login.html')
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
            return render_template('customer_login.html')


@app.route('/customer_edit', methods=['GET', 'POST'])
def customer_edit():
    cust_id = request.cookies.get('cust_id',type=int)
    customer_info = customer.query.filter_by(cust_id=cust_id).first()

    customer_info.cust_fname = request.form.get('Name')
    customer_info.cust_lname = request.form.get('Surname')
    customer_info.cust_phone = request.form.get('Phone')
    customer_info.cust_address = request.form.get('Adress')
    customer_info.cust_bday = request.form.get('Doğum günü')
    db.session.commit()

    return render_template('customer_page.html', customer_info=customer_info)


@app.route('/customer_page', methods=['GET', 'POST'])
def customer_page():
    custlogid = request.cookies.get('cust_id',type=int)
    customer_info =customer.query.filter_by(cust_id = custlogid).first()
    id = request.args.get('id')
    value = request.args.get('value')

    if id == 'editprofile':
        return render_template('customer_edit.html', customer_info=customer_info)

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
    if id == 'purchase_course':
        cust_id = request.cookies.get('cust_id',type=int)
        cust_enrolls = enrolls.query.filter_by(enrolls_prod_id = cust_id, enrolls_course_id = value).first()
        if not cust_enrolls:
            selected_course = course.query.filter_by(course_id = value).first()
            newenroll = enrolls(enrolls_prod_id = cust_id,enrolls_course_id = selected_course.course_id)
            db.session.add(newenroll)
            db.session.commit()

    return render_template('all_courses.html',all_courses=all_courses)

@app.route('/all_courses_related_product', methods=['GET', 'POST'])
def all_courses_related_product():
    return render_template('all_courses_related_product.html')

        
@app.route('/all_products', methods=['GET', 'POST'])
def all_products():
    id = request.args.get('id') #==add_to_Cart ise
    value = request.args.get('value') #product id
    custlogid = request.cookies.get('cust_id',type=int)

    products = product.query.all()
    if id=='add_to_cart':
        added_product= product.query.filter_by(prod_id=int(value)).first()
        cart1 = cart.query.filter_by(cart_cust_id=custlogid,cart_prod_id=int(value)).first()
        if cart1 == None:
            new_cart = cart(cart_cust_id=custlogid,cart_prod_id=int(value),cart_prodcount=1)
            db.session.add(new_cart)
            db.session.commit()
        else:
            print(cart1)
            cart1.cart_prodcount += 1
            db.session.commit()
       

    return render_template('all_products.html',products=products)

@app.route('/carts', methods=['GET', 'POST'])
def carts():
    custid = request.cookies.get('cust_id',type=int)
    id = request.args.get('id') #==delete_from_cart ise
    value = request.args.get('value') #product id
    products_in_cart = cart.query.filter_by(cart_cust_id = custid)
    print(products_in_cart)
    list = []
    countlist = []
    for x in products_in_cart:
        list.append(product.query.filter_by(prod_id = x.cart_prod_id).first())
        countlist.append({'a':x.cart_prod_id,'b':x.cart_prodcount})

    if id=='delete_from_cart':
        selected_product = cart.query.filter_by(cart_cust_id = custid, cart_prod_id = int(value)).first()
        db.session.delete(selected_product)
        db.session.commit()
        list = []
        countlist = []
        for x in products_in_cart:
            products_in_cart = cart.query.filter_by(cart_cust_id = custid)
            list.append(product.query.filter_by(prod_id = x.cart_prod_id).first())
            countlist.append({'a':x.cart_prod_id,'b':x.cart_prodcount})
        return render_template('carts.html',products=list,count=countlist)

    if id=='add_to_order':
        order_totalprice = 0
        order_totalweight = 0
        products_in_cart = cart.query.filter_by(cart_cust_id = custid).all()

        for x in products_in_cart:
            order_totalprice += product.query.filter_by(prod_id = x.cart_prod_id).first().prod_price
            order_totalweight += product.query.filter_by(prod_id = x.cart_prod_id).first().prod_weight
        
        order_quantity = 0
        for x in countlist:
            order_quantity += x.get('b')
   
        order_date = date.today()
        
            
        order_shippingfee = order_totalweight*0.05
        if order_shippingfee < 5:
            order_shippingfee = 5
        order_state = "Hazırlanıyor"

        neworder = orders(order_totalprice=order_totalprice,order_quantity=order_quantity,order_date=order_date,order_totalweight=order_totalweight,order_shippingfee=order_shippingfee,order_state=order_state)
        db.session.add(neworder)
        db.session.commit()
        orderid = orders.query.filter_by(order_totalprice=order_totalprice,order_quantity=order_quantity,order_date=order_date,order_totalweight=order_totalweight,order_shippingfee=order_shippingfee,order_state=order_state).order_by(text("order_id desc")).first().order_id
        for x in products_in_cart:
            newpurchased = purchased(orderid,x.cart_prod_id,custid)
            db.session.add(newpurchased)
            db.session.commit()
        list = []
        countlist = []
        cart.query.filter_by(cart_cust_id = custid).delete()
        return render_template('carts.html',products=list,count=countlist)
    return render_template('carts.html',products=list,count=countlist)


@app.route('/my_courses', methods=['GET', 'POST'])
def my_courses():
    cust_id = request.cookies.get('cust_id',type=int)
    my_enrolls = enrolls.query.filter_by(enrolls_prod_id = cust_id).all()
    list = []
    for x in my_enrolls:
            list.append(course.query.filter_by(course_id = x.enrolls_course_id).first())
    return render_template('my_courses.html',courses=list)


@app.route('/order', methods=['GET', 'POST'])
def order():
    custid = request.cookies.get('cust_id',type=int)
    orderids = purchased.query.filter_by(purchased_cust_id = custid).distinct(purchased.purchased_order_id).all()
    print(orderids)
    return render_template('order.html',orders=orderids)


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