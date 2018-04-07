# Import the Flask class.
# Create an instance of it.
# Pass in the __name__ arguement,
# to indicate the appplication's module.
# Such that Flask knows where to find other
# files such as templates.
from flask import Flask

app = Flask(__name__)

# Load the views.
from app import views