from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Abrir el navegador en la pagina de facebook
driver = webdriver.Edge()
driver.get('https://www.facebook.com')

# Identificar etiquetas para ingresar las credenciales
# Ingresar el correo
correo = driver.find_element(By.XPATH, '//*[@id="email"]')
correo.send_keys('pcuak76@gmail.com')

# Ingresar la clave
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys('hola12345.')

# Buscar el boton de iniciar sesion
btns = driver.find_elements(By.TAG_NAME, 'button')
for btn in btns:
    if btn.get_attribute('name') == 'login':
        time.sleep(2)
        btn.click()
        break

time.sleep(7)
driver.get('https://www.facebook.com/search/posts/?q=Daniel%20Noboa%20Azin%20veronica%20abad')
time.sleep(5)
for i in range(1, 2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
try:
    time.sleep(3)
    contents = driver.find_elements(By.TAG_NAME, 'div')
    for content in contents:
        if 'x193iq5w x1xwk8fm' in content.get_attribute('class'):
            posts = content.find_elements(By.TAG_NAME, 'div')
            for post in posts:
                if 'x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z' == post.get_attribute('class'):
                    driver.execute_script("arguments[0].scrollIntoView(true);", post)
                    containers = post.find_elements(By.TAG_NAME, 'div')
                    for container in containers:
                        if 'html-div xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1iyjqo2' == container.get_attribute('class'):
                            titles = container.find_elements(By.TAG_NAME, 'h3')
                            for title in titles:
                                spans = title.find_elements(By.TAG_NAME, 'span')
                                for span in spans:
                                    if 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs' == span.get_attribute('class'):
                                        print(f'name: {span.text}')
                                    links = span.find_elements(By.TAG_NAME, 'a')
                                    for link in links:
                                        print(f'Perfil: {link.get_attribute("href")}')
                            links = post.find_elements(By.TAG_NAME, 'a')
                            for link in links:
                                print(f'Enlace: {link.get_attribute("href")}')
                                time.sleep(5)
except Exception as ex:
    print(f'Error: {ex}')

input("Esperando que no se cierre webdriver: ")
