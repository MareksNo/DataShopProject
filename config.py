from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'da0caa0551505add1e5a786420a19f1a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_web.db'
db = SQLAlchemy(app)