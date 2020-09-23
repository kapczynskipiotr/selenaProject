import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from seleniumpagefactory.Pagefactory import PageFactory

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15


