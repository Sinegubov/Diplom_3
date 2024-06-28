import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

from helpers.data_generator import UserGenerator
from helpers.api_requests import APIRequests

from data import URL


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
        browser.maximize_window()

    browser.get(URL.BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def password_recovery(driver):
    main_page = MainPage(driver)
    main_page.click_account_button()
    login_page = LoginPage(driver)
    login_page.click_restore_password_button()
    return driver


@pytest.fixture
def forgot_pass_page(password_recovery):
    payload = UserGenerator().generate_user_email()
    driver = password_recovery
    forgot_pass_page = ForgotPasswordPage(driver)
    forgot_pass_page.fill_email_field(payload)
    forgot_pass_page.click_recovery_button()
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
def auth_user(driver, user_data):
    payload, token = user_data
    main_page = MainPage(driver)
    main_page.click_account_button()
    login_page = LoginPage(driver)
    login_page.login(payload["email"], payload["password"])
    return driver


@pytest.fixture
def orders_numbers(user_data):
    payload, token = user_data
    APIRequests.create_order(token)
    APIRequests.create_order(token)
    user_orders = APIRequests.get_user_orders(token)
    orders_numbers = []
    for order in user_orders:
        orders_numbers.append(order["number"])
    return orders_numbers
