from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an Instance of Flask
app = Flask(__name__)
# Include config from config.py
# app.config.from_object('config')

# app.config['SECRET_KEY'] = '520965huang'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:520965huang@utilities-db.coryhpm7bqn1.us-east-1.rds.amazonaws' \
                                        '.com/kerena'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Create an instance of SQLAclhemy
db = SQLAlchemy(app)
