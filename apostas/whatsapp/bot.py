from selenium import webdriver, common
import time
from selenium.webdriver.common.keys import Keys

class WhatsappBot:
    def __init__(self):
        self.conversa = [input('Em qual conversa você quer receber as mensagens?: ')]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome('/Users/leone/Desktop/beto/chromedriver')

    def AbrirWPP(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for conversa in self.conversa:
            campo_conversa = self.driver.find_element_by_xpath(
                f"//span[@title='{conversa}']")
            campo_conversa.click()

    def EnviarMensagens(self, mensagem):
        self.mensagem = mensagem
        chat = self.driver.find_element_by_class_name('_3uMse')
        chat.click()
        chat.send_keys(self.mensagem + Keys.ENTER)
