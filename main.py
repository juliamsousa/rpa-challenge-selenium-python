from selenium import webdriver
from functions import *
import pandas as pd

def main():
    # Criando os diretórios de download da automação
    download_path = r'C:\RPA\rpa-challenge'
    success_directory = create_processing_directory(download_path)

    if success_directory:
        # Definindo as options do Chrome de pasta de download
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {
            "download.default_directory": r'C:\RPA\rpa-challenge'
        })
        # Instanciando um navegador do Chrome com as opções definidas
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        # Chamada da função de navegação para o RPA Challenge
        success_navigate = navigate_rpa_challenge(driver)

        if success_navigate:
            # Baixa o arquivo excel do desafio
            excel_file = download_excel(driver, download_path)

            # Lê o arquivo excel em um DataFrame
            full_file_path = f'{download_path}\\{excel_file}'
            df_data = pd.read_excel(full_file_path)

            # Remove espaços extras no header do DataFrame
            df_data.rename(columns=lambda x: x.strip(), inplace=True)

            if not df_data.empty:
                print("Iniciando o desafio")
                click_on_element(driver, By.XPATH, "//button[text()='Start']")

                for index, row in df_data.iterrows():
                    print("Extraindo os dados da linha")
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    company = row['Company Name']
                    role = row['Role in Company']
                    address = row['Address']
                    email = row['Email']
                    phone_number = row['Phone Number']

                    print("Preenchendo as inputs")
                    set_value_to_input(driver, By.XPATH, '//input[@ng-reflect-name="labelFirstName"]', first_name)
                    set_value_to_input(driver, By.XPATH, '//input[@ng-reflect-name="labelLastName"]', last_name)
                    set_value_to_input(driver, By.XPATH, '//input[@ng-reflect-name="labelCompanyName"]', company)
                    set_value_to_input(driver, By.XPATH, '//input[@ng-reflect-name="labelRole"]', role)
                    set_value_to_input(driver, By.XPATH, '//input[@ng-reflect-name="labelAddress"]', address)
                    set_value_to_input(driver, By.XPATH, '//input[@ng-reflect-name="labelEmail"]', email)
                    set_value_to_input(driver, By.XPATH, '//input[@ng-reflect-name="labelPhone"]', phone_number)

                    print("Clicando no elemento de Submit")
                    click_on_element(driver, By.XPATH, "//input[@value='Submit']")

            message = get_element_value(driver, By.XPATH, "//div[@class[contains(., 'message1')]]")
            succes_rate = get_element_value(driver, By.XPATH, "//div[@class='message2']")

            print('Seu resultado foi:')
            print(f'{message} - {succes_rate}')

main()
