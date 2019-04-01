from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome('C:/Users/hemer/Desktop/Automation/chromedriver')
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print('Teste completo')


def test_geraPessoa(test_setup):
    global nome, cpf, email, celular, cep, numEnd, dtNsc
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
    dtNsc = driver.find_element_by_id('data_nasc').text
    assert dtNsc != ''

#Site Saraiva
def test_cadastraPessoa(test_setup):
    driver.get('https://www.saraiva.com.br/customer/account/create')
    EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Identificação')
    driver.find_element_by_id('firstname_pf').send_keys(nome.split()[0])
    driver.find_element_by_id('lastname').send_keys(nome.split()[2])
    driver.find_element_by_id('email_address_pf').send_keys(email)
    driver.find_element_by_id('password').send_keys('AbC123')
    driver.find_element_by_id('confirmation').send_keys('AbC123')
    driver.find_element_by_id('cpf-number').send_keys(cpf)
    driver.find_element_by_id('gender').click()
    #selecionando sexo, 1 = Masculino, 2 = Feminino
    sexo = Select(driver.find_element_by_id('gender'))
    sexo.select_by_value('1')
    driver.find_element_by_id('fulldob').send_keys(dtNsc)
    driver.find_element_by_id('celular_pf').send_keys(celular)
    driver.find_element_by_id('zip').send_keys(cep)
    time.sleep(2)
    driver.find_element_by_id('address:numero_endereco').send_keys(numEnd)
    driver.find_element_by_id('telephone_pf').send_keys(celular)
