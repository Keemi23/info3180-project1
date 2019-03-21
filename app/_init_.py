from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "m@@dextreme"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://impjobcppvkgbc:5368842d0bd8ebdacf4a628ba3a980c751172c2de7085c23688c8bfe60a37302@ec2-54-83-61-142.compute-1.amazonaws.com:5432/d1r0sbkhohlt2q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views