import time # Выбрал time для удобства тайминга в шагах
from selenium import webdriver
from selenium.webdriver.common.by import By

# Драйвер для Firefox
driver = webdriver.Firefox()
# Открываем сайт
driver.get("https://stellarburgers.nomoreparties.site/")
time.sleep(2)

#Вход через кнопку «Личный кабинет»
button = driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p")
button.click()
time.sleep(2)

#Ввод email
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("itesterovich299@yandex.ru")
time.sleep(1)

#Ввод пароля 6 символов
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("dd1234")
time.sleep(1)

#Нажать на кнопку "Войти"
driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
time.sleep(1)

#Нажать на кнопку «Личный кабинет»
driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()
time.sleep(2)

driver.quit()
