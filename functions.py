from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os, time

def wait_web_element(driver, selector, value, timeout):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((selector, value))
        )
        return True
    except TimeoutException:
        return False

def navigate_rpa_challenge(driver):
    for i in range(1, 4):
        print('Iniciando a navegação para a página do RPA Challenge')
        # Navegando para a página do RPA Challenge
        driver.get('https://rpachallenge.com/')

        try:
            # Verificando se navegou para a página correta pelo título
            WebDriverWait(driver, 10).until(EC.title_contains('Rpa Challenge'))
            print('Navegação realizada com sucesso')
            return True
        except TimeoutException:
            print('Tentando navegar para a página novamente')
            continue

    return False

def create_processing_directory(path):
    for i in range(1, 4):
        print('Criando o diretório informado')
        try:
            os.makedirs(path, exist_ok=True)
            print('Diretório criado com sucesso')
            return True
        except OSError as error:
            print('Tentando criar o diretório novamente')
            continue

    return False

def download_excel(driver, download_path):
    print('Fazendo o download do arquivo Excel de casos para processamento')
    click_on_element(driver, By.XPATH, "//a[contains(., 'Download Excel')]")

    for i in range(30):
        time.sleep(1)
        for File in os.listdir(download_path):
            if File.endswith(".xlsx"):
                return File

    return False

def set_value_to_input(driver, by, input_identifier, value_to_set):
    try:
        element_exists = wait_web_element(driver, by, input_identifier, 5)
        if element_exists:
            driver.find_element(by, input_identifier).send_keys(value_to_set)
            return True
    except Exception:
        return False

def click_on_element(driver, by, element_identifier):
    try:
        element_exists = wait_web_element(driver, by, element_identifier, 5)
        if element_exists:
            driver.find_element(by, element_identifier).click()
            return True
    except Exception:
        return False

def get_element_value(driver, by, element_identifier):
    try:
        element_exists = wait_web_element(driver, by, element_identifier, 5)
        if element_exists:
            return driver.find_element(by, element_identifier).text
    except Exception:
        return False