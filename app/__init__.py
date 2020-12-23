import os
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_s3 import FlaskS3

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

database_url = os.environ.get('DATABASE_URL', None)

if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, '../app.db')
        
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'secret_key'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL') or 'test@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD') or 'test'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['FLASKS3_BUCKET_NAME'] = os.environ.get('FLASKS3_BUCKET_NAME') or None
app.config['FLASKS3_REGION'] = os.environ.get('FLASKS3_REGION') or None

app.config['AWS_DEFAULT_REGION'] = os.environ.get('AWS_DEFAULT_REGION') or 'us-west-2'

mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

s3 = FlaskS3(app)

from app import models, controllers