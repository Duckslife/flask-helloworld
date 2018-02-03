from app import app
from flask import render_template


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
