import pytest

from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from data import URL
from helpers.data_generator import UserGenerator
from helpers.api_requests import APIRequests


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.set_preference('dom.webnotifications.enabled', False)
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
    elif request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-notifications")
        browser = webdriver.Chrome(options=options)

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
    forgot_pass_page.fill_email_field(UserGenerator.generate_user_email())
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


@pytest.fixture
def authorization(driver, user_data):
    payload, token = user_data
    main_page = MainPage(driver)
    main_page.click_personal_account_button()
    login_page = LoginPage(driver)
    login_page.login(payload["email"], payload["password"])
    return driver


# Корректное отображение юникода в параметризованных тестах
def pytest_make_parametrize_id(config, val):
    return repr(val)
