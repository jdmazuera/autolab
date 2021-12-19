from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Response

app = Flask(__name__)
app.config.from_object("app.config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)