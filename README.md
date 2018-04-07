# getting-started-with-flask
Companion code for the getting-started-with-flask-tutorial...

## Stack

- Python
- Virtualenv and virtualenvwrapper
```
pip install virtualenv
pip install virtualenvwrapper
```
- Flask

### Create our app directory
This is where our files will go. Navigate to our app directory. You can name your project whatever you want.
```
mkdir getting-started-with-flask
cd getting-started-with-flask
```

### Create and Activate virtualenv
```
python -m venv env
activate env\Scripts\activate
```

### Install Flask
```
pip install Flask
```
Installing Flask also installs other dependancies, pip freeze to see the list of dependancies.
```
pip freeze
```
Use the following command to store your dependancies to _requirements.txt_ file.

### Create hello_world app
The app should return a _"Hello World!"_ string.

### Run the app
```
set FLASK_APP=run.py
flask run
```
The first command tells the system which app to run, and the second command will start the server. Your should be able to access the application on this address (http://localhost:5000/).