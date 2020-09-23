import pytest
from Config.SeleniumConfiguration import setup
from seleniumpagefactory.Pagefactory import PageFactory
from AutomationPracticeMainPage.AutomationPracticeMainPageElements import AutomationPracticeMainPageElements
from selenium import webdriver
from Config.Helper import helpers


class TestCases():



    # def test1(self, setup):
    #     URL = "http://automationpractice.com/"
    #     self.driver = setup
    #     self.automationPage = AutomationPracticeMainPageElements(self.driver)
    #     self.automationPage.search(URL)

    def test2(self, setup):
        URL = "http://automationpractice.com/"
        product_name = "printed dress"
        self.driver = setup
        self.automationPage = AutomationPracticeMainPageElements(self.driver)
        self.automationPage.search(URL, product_name)
        self.automationPage.addProductToCard()
        print(self.driver.find_element_by_xpath("//*[contains (@class, 'layer_cart_product')]/h2").text)
        assert "Product successfully added to your shopping cart" in self.driver.find_element_by_xpath("//*[contains (@class, 'layer_cart_product')]/h2").text