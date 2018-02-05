from app import app
from flask import render_template, flash, redirect 
from app.forms import login_form

@app.route('/login', methods = ['GET','POST'])
def login():
	form = login_form()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title = 'Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Duckslife'}
	posts = [
		{
			'author':{'username':'john'},
			'body':'test test test test'
		},
		{
			'author':{'username':'sarang'},
			'body': 'test1 test1 test1'
		}
	]
	return render_template('index.html',title='home', user=user, posts=posts)
