from selenium.webdriver.common.by import By

class Locators:
    enter_login_button = (By.XPATH, "//button[text()='Войти в аккаунт']") 
    registration_button = (By.XPATH, "//a[text()='Зарегистрироваться']") 
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input") 
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input") 
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    reg_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    error_password = (By.XPATH, "//p[text()='Некорректный пароль']")
    enter = (By.XPATH, "//h2[text()='Вход']")
    registration = (By.XPATH, "//h2[text()='Регистрация']")
    login_button = (By.XPATH, "//button[text()='Войти']")
    checkout_button = (By.XPATH, "//button[text()='Оформить заказ']")
    personal_acc_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    login_link = (By.XPATH, "//a[@class='Auth_link__1fOlj']")
    recovery_password_button = (By.XPATH, "//a[@href='/forgot-password']")
    recovery_password = (By.XPATH, "//h2[text()='Восстановление пароля']")
    personal_acc_link = (By.XPATH, "//p[text()= 'Личный Кабинет']")
    personal_acc_text = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")
    constructor = (By.XPATH, "//p[text()= 'Конструктор']")
    burger_text = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    exit_button = (By.XPATH, "//button[text()='Выход']")
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    active_tab = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")
    buns = (By.XPATH, "//span[contains(text(), 'Булки')]")
    sauces = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    fillings = (By.XPATH, "//span[contains(text(), 'Начинки')]")