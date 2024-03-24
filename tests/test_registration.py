from faker import Faker
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

fake = Faker()

class TestRegistration:
    def test_registration_true(self, driver: WebDriver):
        name = fake.name()
        email = fake.email()
        password = fake.password()
        driver.find_element(*Locators.enter_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration_button)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration))
        driver.find_element(*Locators.name_input).send_keys(name)
        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.reg_button).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(Locators.enter))
        assert '/login' in driver.current_url

    def test_registration_without_name(self, driver: WebDriver):
        email = fake.email()
        password = fake.password()
        driver.find_element(*Locators.enter_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration_button)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration))
        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.reg_button).click()
        assert '/login' not in driver.current_url

    def test_registration_with_5_symbols(self, driver: WebDriver):
        password = 'abc45'
        driver.find_element(*Locators.enter_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration_button)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration))
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.email_input).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.error_password))