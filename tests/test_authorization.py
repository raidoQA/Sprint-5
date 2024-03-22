from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from const import Constants
from locators import Locators

class TestAuthorization:
    def test_authorization_with_login_account_button(self, driver: WebDriver):
        driver.find_element(*Locators.enter_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.enter))
        driver.find_element(*Locators.email_input).send_keys(Constants.test_email)
        driver.find_element(*Locators.password_input).send_keys(Constants.test_password)

        driver.find_element(*Locators.login_button).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.checkout_button, 'Оформить заказ'))

    def test_authorization_with_personal_acc_button(self, driver: WebDriver):
        driver.find_element(*Locators.personal_acc_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.enter))

        driver.find_element(*Locators.email_input).send_keys(Constants.test_email)
        driver.find_element(*Locators.password_input).send_keys(Constants.test_password)
        driver.find_element(*Locators.login_button).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.checkout_button, 'Оформить заказ'))

    def test_authorization_in_registration_form(self, driver: WebDriver):
        driver.find_element(*Locators.enter_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration_button)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.registration))

        driver.find_element(*Locators.login_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.enter))
        driver.find_element(*Locators.email_input).send_keys(Constants.test_email)
        driver.find_element(*Locators.password_input).send_keys(Constants.test_password)
        driver.find_element(*Locators.login_button).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.checkout_button, 'Оформить заказ'))

    def test_authorization_in_password_recovery_form(self, driver: WebDriver):
        driver.find_element(*Locators.enter_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.recovery_password_button)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.recovery_password))

        driver.find_element(*Locators.login_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.enter))

        driver.find_element(*Locators.email_input).send_keys(Constants.test_email)
        driver.find_element(*Locators.password_input).send_keys(Constants.test_password)
        driver.find_element(*Locators.login_button).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(Locators.checkout_button, 'Оформить заказ'))
