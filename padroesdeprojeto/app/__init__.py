from flask import Flask
from dynaconf import FlaskDynaconf
from mvc_flask import FlaskMVC

from .blueprint import home


def create_app():
    app = Flask(__name__)
    FlaskMVC(app, 'padroesdeprojeto')
    FlaskDynaconf(app, extensions_list=True)

    
    return app