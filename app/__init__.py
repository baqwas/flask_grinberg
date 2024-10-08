#!/usr/bin/env python3

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # database
migrate = Migrate(app, db)  # migration engine

from app import routes, models  # structure of the database