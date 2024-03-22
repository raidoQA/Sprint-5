from selenium.webdriver.chrome.webdriver import WebDriver
from locators import Locators
from const import Constants

class TestSectionConstructor:

    def test_section_sauces(self, driver: WebDriver):
        sauces = driver.find_element(*Locators.sauces)
        sauces.click()
        assert Constants.new_class in sauces.get_attribute("class")

    def test_section_fillings(self, driver: WebDriver):
        fillings = driver.find_element(*Locators.fillings)
        fillings.click()
        assert Constants.new_class in fillings.get_attribute("class")

    def test_section_buns(self, driver: WebDriver):
        fillings = driver.find_element(*Locators.fillings)
        fillings.click()
        buns = driver.find_element(*Locators.buns)
        buns.click()
        assert Constants.new_class in buns.get_attribute("class")