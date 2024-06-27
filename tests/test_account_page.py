import allure

from pages.order_history_page import OrderHistoryPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

from data import URL


@allure.feature("Личный кабинет")
class TestAccount:
    @allure.title("Тест перехода по клику на Личный кабинет")
    @allure.description("Переходим в ЛК пользователя и сверяем текущую страницу с константой по URL")
    def test_transfer_to_account_on_click(self, auth_user):
        driver = auth_user
        main_page = MainPage(driver)
        main_page.click_account_button()
        profile_page = AccountPage(driver)
        current_url = profile_page.check_transfer_to_account()

        assert current_url == URL.PROFILE_URL

    @allure.title("Тест перехода в Историю заказов по клику")
    @allure.description("Переходим в  Историю заказов и сверяем текущую страницу с константой по URL")
    def test_transfer_to_order_history_on_click(self, auth_user):
        driver = auth_user
        main_page = MainPage(driver)
        main_page.click_account_button()
        profile_page = AccountPage(driver)
        profile_page.click_order_history_button()
        order_history_page = OrderHistoryPage(driver)
        current_url = order_history_page.check_transfer_to_order_history()

        assert current_url == URL.ORDER_HISTORY_URL

    @allure.title("Тест выхода из аккаунта")
    @allure.description("Выходим из аккаунта и сверяем текущую страницу с константой по URL")
    def test_logout(self, auth_user):
        driver = auth_user
        main_page = MainPage(driver)
        main_page.click_account_button()
        order_history_page = OrderHistoryPage(driver)
        order_history_page.click_log_out_button()
        login_page = LoginPage(driver)
        current_url = login_page.check_switch_on_login_page()

        assert current_url == URL.LOGIN_URL
