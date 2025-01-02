from ward import fixture
from splinter import Browser

from padroesdeprojeto.app import create_app

@fixture
def browser_client():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()

    browser = Browser('flask',app=app)

    return browser