from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"nickname":"Musu"} # fake user
    posts = [ #fake array of posts
        {
            'author':{'nickname':'Abdulvahab'},
            'body': 'Beautiful day in Oxford!'
        },
        {
            'author':{'nickname':'Fatema'},
            'body': 'I did my first fast today!'
        },
        {
            'author':{'nickname':'Abdulrehman'},
            'body': 'I love Cricket'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
