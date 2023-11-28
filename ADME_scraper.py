from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Properties():
    def __init__(self):
        Options = webdriver.EdgeOptions()
        Options.add_argument('--headless')
        Options.add_argument('disable-gpu')
        self.driver = webdriver.Edge(executable_path='msedgedriver.exe', options=Options)
    def SwissADME(self,smiles):
        self.driver.get('http://www.swissadme.ch/index.php')
        smiles_input = self.driver.find_element(By.XPATH, '//*[@id="smiles"]')
        smiles_input.send_keys(smiles)
        smiles_input.send_keys(Keys.RETURN)
        sleep(10)
        run = self.driver.find_element(By.XPATH, '//*[@id="submitButton"]')
        print(run.is_enabled)
        run.click()
        data=[]
        sleep(10)
        with open('xpath_swissADME.txt','r',encoding='utf-8') as properties_file:
            properties = properties_file.read().split('\n')
            for xpath in properties:
                data_element = self.driver.find_element(By.XPATH,f'{xpath}')
                print(data_element.get_attribute('innerHTML'))
                data.append(data_element.get_attribute('innerHTML'))
            properties_file.close()
        return data
    def PreADME(self,mol):
        self.driver.get('https://preadmet.webservice.bmdrc.org/adme/')
        input_button = self.driver.find_element(By.XPATH, '//*[@id="sketcher_button_open"]')
        input_button.click()
        input = self.driver.find_element(By.XPATH, '//*[@id="sketcher_load_dialog_ta"]')
        input.send_keys(mol)
        input.send_keys(Keys.RETURN)
        load = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/button")
        load.click()
        submit = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div[4]/div[2]/div/div/div/div/input')
        submit.click()
        data = []
        sleep(10)
        with open('xpath_preADMET','r',encoding='utf-8') as properties_file:
            properties = properties_file.read().split('\n')
            for xpath in properties:
                data_element = self.driver.find_element(By.XPATH, f'{xpath}')
                print(data_element.get_attribute('innerHTML'))
                data.append(data_element.get_attribute('innerHTML'))
            properties_file.close()
        return data
    def Toxicity(self,mol):
        self.driver.get('https://preadmet.webservice.bmdrc.org/toxicity/')
        input_button = self.driver.find_element(By.XPATH, '//*[@id="sketcher_button_open"]')
        input_button.click()
        input = self.driver.find_element(By.XPATH, '//*[@id="sketcher_load_dialog_ta"]')
        input.send_keys(mol)
        input.send_keys(Keys.RETURN)
        load = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/button")
        load.click()
        submit = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div/div[4]/div[2]/div/div/div/div/input')
        submit.click()
        data = []
        sleep(10)
        with open('xpath_Toxicity','r',encoding='utf-8') as properties_file:
            properties = properties_file.read().split('\n')
            for xpath in properties:
                data_element = self.driver.find_element(By.XPATH, f'{xpath}')
                print(data_element.get_attribute('innerHTML'))
                data.append(data_element.get_attribute('innerHTML'))
            properties_file.close()
        return data
