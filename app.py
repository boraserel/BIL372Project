from flask import Flask, render_template
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