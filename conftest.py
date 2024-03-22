import pytest
from selenium import webdriver
from const import Constants
from selenium.webdriver.chrome.webdriver import WebDriver
from const import Url
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.url)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver: WebDriver):
    driver.find_element(*Locators.enter_login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.enter))
    driver.find_element(*Locators.email_input).send_keys(Constants.test_email)
    driver.find_element(*Locators.password_input).send_keys(Constants.test_password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.text_to_be_present_in_element(Locators.checkout_button, 'Оформить заказ'))
    return driver