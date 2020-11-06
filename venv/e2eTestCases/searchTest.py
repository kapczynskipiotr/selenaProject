import pytest
from Config.SeleniumConfiguration import chrome_setup
from seleniumpagefactory.Pagefactory import PageFactory
from AutomationPracticeMainPage.AutomationPracticeMainPageElements import AutomationPracticeMainPageElements
from selenium import webdriver
from Config.Helper import helpers
from Config.SeleniumConfiguration import BaseTest

URL = "http://automationpractice.com/"
product_name = "printed dress"


class TestCases(BaseTest):

    def test_userSearchProductAndBuyByAddToCartOnProductPopup(self, chrome_setup):


        self.automationPage = AutomationPracticeMainPageElements(self.driver)

        self.automationPage.search(URL, product_name)
        self.automationPage.addProductToCard()
        self.helpers = helpers(self.driver)
        self.helpers.fluentWait("//*[contains (@class, 'layer_cart_product')]/h2")

        print(self.driver.find_element_by_xpath("//*[contains (@class, 'layer_cart_product')]/h2").text)
        assert "Product successfully added to your shopping cart" in self.driver.find_element_by_xpath(
            "//*[contains (@class, 'layer_cart_product')]/h2").text
        self.driver.quit()

