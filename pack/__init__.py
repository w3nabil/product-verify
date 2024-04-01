"""
This module contains the package initialization function and the main flask app function.
Author: NABIL 
Date: 29/03/2024
"""

from os import getenv, path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()

app = Flask(__name__, template_folder='public', static_folder='src')

# App configuration, Registering Blue Print and database initialization
def server():
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{getenv('uri')}"
    app.config['SECRET_KEY'] = f"{getenv('secret')}"
    db.init_app(app)
    from .sqlite import Product
    
    with app.app_context():
        create_db()
    
    from .views import views
    app.register_blueprint(views)

    return app

# If db doesn't exist, create it
def create_db():
    if not path.exists('pack/product.db'):
        db.create_all()
        print('Database Created')
