from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID ="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form= form,
                           providers=app.config['OPENID_PROVIDERS'])
