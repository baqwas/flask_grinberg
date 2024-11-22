# Reference
These notes were prepared during self-paced learning. Over 20 years ago, I used to practice Flask tutorials based on Microsoft webinars! Unfortunately, I never had the bandwidth to practice what I learned. Now, with enforced involuntary retirement, I can indulge in nostalgia.  

This document uses examples from Miguel Grinberg as illustrated in his Flask Mega-Tutorial (new and improved edition, of course):  
Flask Web Development by Miguel Grinberg, (O’Reilly). Copyright 2014 Miguel Grinberg, 978-1-449-3726-2.  

# flask
Flask deployment and basic exercises

## Clone repository
https://github.com/baqwas/flask

## Create virtual environment
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements

## Install Flask Python package
Either (lame):  
`(venv) $ pip import flask`   
Or:  
Drill-down (left-nav pane) *-->* Python Packages *-->* Search *-->* flask *-->* Install *-->* choose version  
wait for confirmation message

## Install dotenv Python package
Drill-down (left-nav pane) *-->* Python Packages *-->* Search *-->* dotenv *-->* Install *-->* choose version
wait for confirmation message

## Create folder hello

## Create script __init__.py
Create a Python script file, `__init__.py`, under the folder, `app`, as follows:  

```
from flask import Flask
app = Flask(__name__)
from app import routes
```

## Create environment variables
In file `.flaskenv` (under the top folder for the project), append the following entry:  

```
FLASK_APP=helloapp.py
```

## Run the Flask application instance
Either  
`flask run`  
Or  
`flask helloapp.py`  
