from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome("C:/Users/Piotrek/PycharmProjects/selenaProject/chromedriver.exe")
    driver.maximize_window()
    return driver