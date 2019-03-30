from selenium import webdriver
import time
import pytest


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome('C:/Users/hemer/Desktop/Automation/chromedriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print('Teste completo')


def test_geraPessoa(test_setup):
    global nome, cpf, email, celular, cep, numEnd
    driver.get('https://www.4devs.com.br/gerador_de_pessoas')
    driver.find_element_by_id('bt_gerar_pessoa').click()
    time.sleep(3)
    nome = driver.find_element_by_id('nome').text
    assert nome != ''
    cpf = driver.find_element_by_id('cpf').text
    assert cpf != ''
    email = driver.find_element_by_id('email').text
    assert email != ''
    celular = driver.find_element_by_id('celular').text
    assert celular != ''
    cep = driver.find_element_by_id('cep').text
    assert cep != ''
    numEnd = driver.find_element_by_id('numero').text
    assert numEnd != ''

#Site Saraiva
def test_cadastraPessoa(test_setup):
    driver.get('https://www.saraiva.com.br/customer/account/create')
    driver.find_element_by_id('firstname').send_keys(nome)

'''def test_teardown():
    driver.close()
    driver.quit()
    print('Teste completo')'''