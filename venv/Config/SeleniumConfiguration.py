from selenium import webdriver
import pytest

firefoxPath = "C:/Users/Piotrek/PycharmProjects/selenaProject/geckodriver.exe"

@pytest.fixture()
def setup():

    # driver = webdriver.Chrome("C:/Users/Piotrek/PycharmProjects/selenaProject/chromedriver.exe")
    driver = webdriver.Firefox(executable_path=firefoxPath)
    driver.maximize_window()
    return driver
