from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def send_whatsapp_message(phone_number, message):

    # Formatando a mensagem para evitar envio prematuro ao detectar quebra de linha
    # Substitui '\n' por SHIFT+ENTER para criar uma nova linha sem enviar a mensagem
    #message = message.replace("U+E007", "/n")
    
    driver = webdriver.Chrome()  # Substitua por GeckoDriver para Firefox, se necessário
    baseurl = "https://web.whatsapp.com/"
    driver.get(baseurl)
    time.sleep(60)  # Espera o usuário fazer login com o QR code
    
    search_box_path = ('//div[@contenteditable="true"][@data-tab="3"]')
    message_box_path = ('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

    try:
        search_box = driver.find_element("xpath", search_box_path)
        search_box.send_keys(phone_number + Keys.ENTER)
        time.sleep(5)
        
        
        
        message_box = driver.find_element("xpath", message_box_path)
        message_box.click()
        
        #ActionChains(driver)\
        #.send_keys_to_element(message_box, message)\
        #.perform()
        

        for line in message.split('\n'):
            ActionChains(driver).send_keys(line).perform()
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            ActionChains(driver).send_keys(Keys.RETURN).perform()


        #message_box = driver.find_element("xpath", message_box_path)
        #message_box.send_keys("Hello" + Keys.TAB + "World" + Keys.ENTER)        

        print("Mensagem enviada")
        time.sleep(200)

    except Exception as e:
        print("Erro ao enviar a mensagem no WhatsApp:", e)

    finally:
        driver.quit()


