from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URLS de acesso da Betfair
url = 'https://www.betfair.com/exchange/plus/'
url2 = 'https://bit.ly/3IsglH8'

# Definições do firefox
caps = {'browserName': 'firefox',
        'zal:name': 'myTestName',
        'zal:build': 'myTestBuild'}

# Caminhos xpath do selenium
xpath_login = "//div[@class='ssc-lifg']//input[@name='username']"
xpath_password = "//*[@id='ssc-lipw']"
xpath_elementos = "//div[@class='lobby-table__wrapper']"
xpath_elementos2 = "//div[@class='lobby-table__wrapper lobby-table__wrapper_active']"

# Login e senha da Betfair
login = ""
password = ""


class Driver:
    def __init__(self):
        self.driver = webdriver.Firefox(capabilities=caps)
        self.acesso_bet()

    def acesso_bet(self):
        self.driver.get(url)
        time.sleep(5)
        self.driver.find_element(By.XPATH, value=xpath_login).send_keys(login)
        time.sleep(1)
        self.driver.find_element(By.XPATH, value=xpath_password).send_keys(password + Keys.ENTER)
        time.sleep(5)
        self.driver.get(url2)
        time.sleep(20)
        self.driver.maximize_window()
        time.sleep(1)

    def reset_driver(self):
        self.driver.close()
        time.sleep(2)
        self.driver.__init__()
        time.sleep(2)
        self.acesso_bet()

    def pegar_elementos(self):
        while True:
            try:
                elementos = self.driver.find_elements(By.XPATH, value=xpath_elementos)
                elementos_exc = self.driver.find_elements(By.XPATH, value=xpath_elementos2)
                elementos_html = []
                for k in range(len(elementos_exc)):
                    elementos.append(elementos_exc[k])
                for k in range(len(elementos)):
                    elementos_html.append(elementos[k].get_attribute('outerHTML'))
                return elementos_html
            except:
                continue
