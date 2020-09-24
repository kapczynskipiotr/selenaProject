import pytest
from Config.SeleniumConfiguration import setup
from seleniumpagefactory.Pagefactory import PageFactory
from AutomationPracticeMainPage.AutomationPracticeMainPageElements import AutomationPracticeMainPageElements
from selenium import webdriver
from Config.Helper import helpers

URL = "http://automationpractice.com/"
product_name = "printed dress"


class TestCases():

    def test_userSearchProductAndBuyByAddToCartOnProductPopup(self, setup):
        self.driver = setup
        self.automationPage = AutomationPracticeMainPageElements(self.driver)
        self.automationPage.search(URL, product_name)
        self.automationPage.addProductToCard()
        self.helpers = helpers(self.driver)
        self.helpers.fluentWait("//*[contains (@class, 'layer_cart_product')]/h2")

        print(self.driver.find_element_by_xpath("//*[contains (@class, 'layer_cart_product')]/h2").text)
        assert "Product successfully added to your shopping cart" in self.driver.find_element_by_xpath(
            "//*[contains (@class, 'layer_cart_product')]/h2").text
        self.driver.quit()
