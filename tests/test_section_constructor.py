from selenium.webdriver.chrome.webdriver import WebDriver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSectionConstructor:

    def test_section_sauces(self, driver: WebDriver):
        sauces = driver.find_element(*Locators.sauces)
        sauces.click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.active_tab))
        assert driver.find_element(*Locators.active_tab).text == 'Соусы'

    def test_section_fillings(self, driver: WebDriver):
        fillings = driver.find_element(*Locators.fillings)
        fillings.click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.active_tab))
        assert driver.find_element(*Locators.active_tab).text == 'Начинки'

    def test_section_buns(self, driver: WebDriver):
        fillings = driver.find_element(*Locators.fillings)
        fillings.click()
        buns = driver.find_element(*Locators.buns)
        buns.click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.active_tab))
        assert driver.find_element(*Locators.active_tab).text == 'Булки'