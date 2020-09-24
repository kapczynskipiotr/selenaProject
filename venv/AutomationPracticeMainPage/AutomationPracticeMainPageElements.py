from seleniumpagefactory.Pagefactory import PageFactory
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Config.Helper import helpers

search_bar = "//input[contains (@id, 'search_query_top')]"
search_result = "//div[contains (@class, 'ac_results')]"
search_confirm_button = "//form[contains (@id, 'searchbox')]/button"
product_on_search_result = "//span[contains (text(), '$28.98')]/ancestor::div[contains (@class, 'product-container')]"
quick_view_product_button = "//span[contains (text(), 'Quick view')]"


class AutomationPracticeMainPageElements():
    def __init__(self, driver):
        self.driver = driver

    def search(self, url, product_name):
        self.helpers = helpers(self.driver)
        self.driver.get(url)
        self.getUrl = self.driver.current_url
        self.driver.find_element_by_xpath(search_bar).send_keys(product_name)

        self.helpers.fluentWait(search_result)

        self.driver.find_element_by_xpath(search_confirm_button).click()

    def addProductToCard(self):
        self.helpers.fluentWait(product_on_search_result)

        product = self.driver.find_element_by_xpath(product_on_search_result)
        action = ActionChains(self.driver)
        action.move_to_element(product).perform()
        self.helpers.waitAndClick(quick_view_product_button)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[contains (@id, 'fancybox-frame')]"))

        self.helpers = helpers(self.driver)
        self.helpers.fluentWait("//*[contains (@id, 'add_to_cart')]")

        self.driver.find_element_by_xpath("//*[contains (@id, 'add_to_cart')]").click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains (@class, 'icon-ok')]"))
        )

        # self.search_box.set_text('pants')
        # self.search_result_of_search_box.click_button()

        # elements = AutomationPracticeMainPageElements
        # driver.quit()
