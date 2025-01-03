from flask import Flask
from dynaconf import FlaskDynaconf
from mvc_flask import FlaskMVC
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()




def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)
    else:
        app.config.from_object(Config)

    FlaskMVC(app, 'padroesdeprojeto')
    # FlaskDynaconf(app, extensions_list=True)
    db.init_app(app)

    
    return app