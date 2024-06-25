import pytest

from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_pass_page import ForgotPasswordPage
from data import URL
from helpers.data_generator import UserGenerator
from helpers.api_requests import APIRequests


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    if request.param == "firefox":
        browser = webdriver.Firefox()
        browser.get(URL.BASE_URL)
    elif request.param == "chrome":
        browser = webdriver.Chrome()
        browser.get(URL.BASE_URL)

    yield browser
    browser.quit()


@pytest.fixture
def password_recovery(driver):
    main_page = MainPage(driver)
    main_page.click_personal_account_button()
    login_page = LoginPage(driver)
    login_page.click_restore_password_button()
    return driver


@pytest.fixture
def forgot_pass_page(password_recovery):
    driver = password_recovery
    forgot_pass_page = ForgotPasswordPage(driver)
    forgot_pass_page.click_email_field()
    forgot_pass_page.set_email(UserGenerator.generate_user_email())
    forgot_pass_page.click_recover_button()
    return driver


@pytest.fixture
def user_data():
    data = []
    payload = UserGenerator().generate_user_info()
    token = APIRequests.get_token(payload)
    data.append(payload)
    data.append(token)

    yield data
    APIRequests.delete_user(token)

# Корректное отображение юникода в параметризованных тестах


def pytest_make_parametrize_id(config, val):
    return repr(val)
