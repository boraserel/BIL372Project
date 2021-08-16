from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from model import db, app
from model import course,instructor
from flask_sqlalchemy import SQLAlchemy

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Content',
        'date_posted': 'Aug 14, 2021'
    },
    {
        'author': 'Borahan Serel',
        'title': 'Blog Post 2',
        'content': 'Second Content',
        'date_posted': 'Aug 15, 2021'
    }
]



@app.route("/")
def home():
    return render_template('login.html',posts=posts)

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
            print("deneee")
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')


    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page

    instructor_info = {
        'InstructorID': '1234567',
        'Name': 'Oğuz',
        'Surname': 'Ergin',
        'Contact': 'oergin@etu.edu.tr',
        'Phone': '5335242415',
        'Average_Rate': '1'}
    courses_by_instructor= [{
        'CourseID': '111111',
        'Name': 'Mimari',
        'Category': 'Computer Science',
        'Level': '6',
        'Price': '500',
        'Duration': '12'},{
        'CourseID': '22222',
        'Name': 'Bahçivanlık',
        'Category': 'Bahçe',
        'Level': '3',
        'Price': '200',
        'Duration': '5'},{
        'CourseID': '333333',
        'Name': 'Antik Kazıcılık',
        'Category': 'Arkeoloji',
        'Level': '7',
        'Price': '600',
        'Duration': '30'}]

    return render_template('instructor_page.html',instructor_info=instructor_info,courses_by_instructor=courses_by_instructor)



@app.route('/instructor_page', methods=['GET', 'POST'])
def instructor_page():
    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page
    id = request.args.get('id')
    value= request.args.get('value')
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
        selected_course={
        'CourseID': '111111',
        'Name': 'Mimari',
        'Category': 'Computer Science',
        'Level': '6',
        'Price': '500',
        'Duration': '12'}
        return render_template('instructor_edit.html',instructor_info=instructor_info,selected_course=selected_course)

@app.route('/instructor_edit', methods=['GET', 'POST'])
def instructor_edit():
    if request.method == 'POST':
             eID=request.form.get('CourseID')
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
