from selenium.webdriver.chrome.webdriver import WebDriver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccount:

    def test_constructor_from_personal_account(self, login: WebDriver):
        login.find_element(*Locators.personal_acc_link).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.personal_acc_text))
        login.find_element(*Locators.constructor).click()
        assert WebDriverWait(login, 3).until(expected_conditions.text_to_be_present_in_element(Locators.burger_text, 'Соберите бургер'))

    def test_constructor_from_personal_account_with_logo_button(self, login: WebDriver):
        login.find_element(*Locators.personal_acc_link).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.personal_acc_text))
        login.find_element(*Locators.logo).click()
        assert WebDriverWait(login, 3).until(expected_conditions.text_to_be_present_in_element(Locators.burger_text, 'Соберите бургер'))

    def test_exit(self, login: WebDriver):
        login.find_element(*Locators.personal_acc_link).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.personal_acc_text))
        login.find_element(*Locators.exit_button).click()
        assert WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.enter))