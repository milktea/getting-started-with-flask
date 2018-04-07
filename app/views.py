# Create a function that will display
# the 'Hello World string.'
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
