from selenium import webdriver
from time import sleep


# Inicializar ChromeDriver
driver = webdriver.Chrome()

# Navegar a una página web
driver.get("http://www.yahoo.com")
sleep(10)
print('funciona todo')
# Verificar el título de la página
assert "Google" in driver.title

# Cerrar el navegador
driver.quit()
