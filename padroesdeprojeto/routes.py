from mvc_flask import Router
from flask import render_template
from padroesdeprojeto.controllers.home_controller import HomeController



Router.get('/', 'home#index')

