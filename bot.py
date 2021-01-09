from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random



def login(browser):
    browser.get('https://www.instagram.com/?hl=es')
    time.sleep(3)
    user = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")

    user.send_keys("")
    password.send_keys("")
    login.click()
    time.sleep(30)
    # browser.get('https://www.instagram.com/p/CJrQoUopbwp/') #Capiscci
    # browser.get('https://www.instagram.com/p/BnU29VWljFO/') #Mio
    time.sleep(2)

    
    

def main():
    browser = webdriver.Firefox()
    login(browser)
    comentar(browser)


def comentar(browser):
    for i in range(20):
        for i in range(10):
            cadena = leer_cuentas()
            encontrar_caja_comentario = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
            caja_comentario = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(cadena)
            time.sleep(2)
            boton_comentar = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
            time.sleep(random.randint(30,40))
        # browser.get('https://www.instagram.com/p/CJrQoUopbwp/') #Capiscci
        time.sleep(200)


def leer_cuentas():
    with open(r'cuentas.txt', 'r') as f:
        commentsl = [line.strip() for line in f]
    comments = commentsl
    
    usuario1 = random.choice(comments)
    comments.remove(usuario1)
    usuario2 = random.choice(comments)   

    return usuario1 + " "+ usuario2


main()


