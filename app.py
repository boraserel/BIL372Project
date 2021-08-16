from flask import Flask, request, flash, url_for, redirect, render_template, make_response
app = Flask(__name__)

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

@app.route('/instructor_page', methods=['GET', 'POST'])
def instructor_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

    #if username and password are not in database redirect instructor page
    #return render_template('instructor_login.html')
    #else redirect instructor page
    return render_template('instructor_page.html')

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
