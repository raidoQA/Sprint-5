import time # Выбрал time для удобства тайминга в шагах
from selenium import webdriver
from selenium.webdriver.common.by import By

# Драйвер для Firefox
driver = webdriver.Firefox()
# Открываем сайт
driver.get("https://stellarburgers.nomoreparties.site/")
time.sleep(2)

#Вход по кнопке "Войти в аккаунт"
button = driver.find_element(By.CLASS_NAME, "button_button__33qZ0")
button.click()
time.sleep(2)

#Регистрация нового пользователя
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

#Ввод имени
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Андрей")
time.sleep(1)
#Ввод email
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("itesterovich302@yandex.ru")
time.sleep(1)

#Ввод пароля менее 6 символов
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("dd12")
time.sleep(1)

#Нажать на кнопку "Зарегистрироваться"
driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
time.sleep(2)


driver.quit()
