from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *


class helpers():
    def __init__(self, driver):
        self.driver = driver

    def waitAndClick(self, pageElemenet):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pageElemenet))
        )
        self.driver.find_element_by_xpath(pageElemenet).click()

    def fluentWait(self, pageElement):
        fluent_wait = WebDriverWait(self.driver, 10, 1,
                                    [ElementNotVisibleException, ElementNotSelectableException])
        element = fluent_wait.until(EC.element_to_be_clickable((By.XPATH, pageElement)))
