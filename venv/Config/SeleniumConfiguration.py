from selenium import webdriver
import pytest

firefoxPath = "C:/Users/Piotrek/PycharmProjects/selenaProject/geckodriver.exe"



@pytest.fixture(params=["chrome"], scope='class')

def chrome_setup(request):
    if request.param =="chrome":
        driver = webdriver.Chrome("C:/Users/Piotrek/PycharmProjects/selenaProject/chromedriver.exe")
        request.cls.driver = driver
        driver.maximize_window()

    if request.param =="firefox":
        driver = webdriver.Firefox(executable_path=firefoxPath)
        driver.maximize_window()
    yield

@pytest.mark.usefixtures("chrome_setup")
class BaseTest:
    pass
