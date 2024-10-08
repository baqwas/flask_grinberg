from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'El Doktor'}
    posts = [
        {
            'author': {'username': 'Samuel'},
            'body': 'Beautiful day in Seattle!'
        },
        {
            'author': {'username': 'Meister'},
            'body': 'The Matrix movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)