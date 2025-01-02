from ward import test

from tests.fixtures import browser_client

@test('visitante visita pagina inicial com sucesso')
def _(browser = browser_client):
    
    browser.visit('/')

    assert browser.status_code == 200
    assert browser.is_text_present('home page')