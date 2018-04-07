# Create a function that will display
# the 'Hello World string.'
from app import app

@app.route('/')
@app.route('/index')
def index():
	return 'Hello World!'
