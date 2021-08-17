from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from model import db, app, instructorlogin
from model import course,instructor
from flask_sqlalchemy import SQLAlchemy


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
                response.set_cookie("inst_id", str(instructor.inst_id))
                return response

            else:
                flash('Incorrect Email or Password')
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
    courses = course.query.filter_by(course_inst_id=inst.inst_id).all()
    if id == 'deletebutton':
        course_toBeDeleted = course.query.filter_by(course_id = value).first()
        print('ASDASDASDASD')
        db.session.delete(course_toBeDeleted)
        db.session.commit()

    instructor_info = {
        'InstructorID': '1234567',
        'Name': 'Oğuz',
        'Surname': 'Ergin',
        'Contact': 'oergin@etu.edu.tr',
        'Phone': '5335242415',
        'Average_Rate': '1'}
    courses_by_instructor = [{
        'CourseID': '111111',
        'Name': 'Mimari',
        'Category': 'Computer Science',
        'Level': '6',
        'Price': '500',
        'Duration': '12'}, {
        'CourseID': '22222',
        'Name': 'Bahçivanlık',
        'Category': 'Bahçe',
        'Level': '3',
        'Price': '200',
        'Duration': '5'}, {
        'CourseID': '333333',
        'Name': 'Antik Kazıcılık',
        'Category': 'Arkeoloji',
        'Level': '7',
        'Price': '600',
        'Duration': '30'}]

    #if id= delete delete row where id = value and render below
    if id=="deletebutton" :
        #delete
        return render_template('instructor_page.html',instructor_info=instructor_info,courses_by_instructor=courses_by_instructor)
    #if id= edit get row datas where id=value and render edit page with selected row parameters.
    if id=="editbutton":
        #course id oldugu row
        selected_course= course.query.filter_by(course_id = value).first()
        return render_template('instructor_edit.html',instructor_info=instructor_info,selected_course=selected_course)

@app.route('/instructor_edit', methods=['GET', 'POST'])
def instructor_edit():
    if request.method == 'POST':
             eID=request.form.get('CourseID') #course id cannot change
             eName= request.form.get('Name')
             eCategory = request.form.get('Category')
             eLevel = request.form.get('Level')
             ePrice = request.form.get('Price')
             eDuration = request.form.get('Duration')

    #course tablosunu degistir.
    #course idden instructor  id bul
    #instructor id den courseları bul ve instructor page renderla
    instructor_info = {
        'InstructorID': '1234567',
        'Name': 'Oğuz',
        'Surname': 'Ergin',
        'Contact': 'oergin@etu.edu.tr',
        'Phone': '5335242415',
        'Average_Rate': '1'}
    courses_by_instructor = [{
        'CourseID': '111111',
        'Name': 'Mimari',
        'Category': 'Computer Science',
        'Level': '6',
        'Price': '500',
        'Duration': '12'}, {
        'CourseID': '22222',
        'Name': 'Bahçivanlık',
        'Category': 'Bahçe',
        'Level': '3',
        'Price': '200',
        'Duration': '5'}, {
        'CourseID': '333333',
        'Name': 'Antik Kazıcılık',
        'Category': 'Arkeoloji',
        'Level': '7',
        'Price': '600',
        'Duration': '30'}]
    return render_template('instructor_page.html', instructor_info=instructor_info,courses_by_instructor=courses_by_instructor)

    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page
    return render_template('customer_page.html')

@app.route('/customer_page_checkin', methods=['GET', 'POST'])
def customer_page_checkin():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page
    customer_info = {
        'cust_id': '111111',
        'cust_fname': 'bugra',
        'cust_lname': 'yalcib',
        'cust_phone': '53142413',
        'cust_address': 'ankara',
        'cust_bday': '12.09.2077'}
    return render_template('customer_page.html',customer_info=customer_info)

@app.route('/customer_page', methods=['GET', 'POST'])
def customer_page():
    customer_info = {
        'cust_id': '111111',
        'cust_fname': 'bugra',
        'cust_lname': 'yalcib',
        'cust_phone': '53142413',
        'cust_address': 'ankara',
        'cust_bday': '12.09.2077'}
    return render_template('customer_page.html',customer_info=customer_info)

@app.route('/all_courses', methods=['GET', 'POST'])
def all_courses():
    if request.method == 'POST':
        searched_course = request.form.get('search_bar')  # course id cannot change
        print(searched_course)



    all_courses = [{
        'course_id': '111111',
        'course_name': 'Mimari',
        'course_category': 'Computer Science',
        'course_level': '6',
        'course_price': '500',
        'course_duration': '12',
        'course_inst_id': '1'}]

    return render_template('all_courses.html',all_courses=all_courses)



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
