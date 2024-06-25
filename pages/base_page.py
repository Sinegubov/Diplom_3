import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import URL
from factory import WebdriverFactory as WD


class BasePage:

    def __init__(self, wd):
        self.wd = wd

    @allure.step("Открыть базовую страницу")
    def open_base_url(self):
        self.WD.getWebdriver.get(URL.BASE_URL)