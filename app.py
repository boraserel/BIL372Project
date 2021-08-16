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
    return render_template('instructor_page.html',instructor_info=instructor_info,courses_by_instructor=courses_by_instructor)


@app.route('/customer_page', methods=['GET', 'POST'])
def customer_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page
    return render_template('customer_page.html')

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
