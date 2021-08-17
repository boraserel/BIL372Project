from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from model import db, app, instructorlogin, needed
from model import course,instructor,enrolls,needed
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update


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