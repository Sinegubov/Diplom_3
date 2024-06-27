import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
# from pages.order_history_page import OrderHistoryPage
# from pages.login_page import LoginPage
from data import URL


@allure.feature("Личный кабинет")
class TestAccount:
    @allure.title("Тест перехода в ЛК по клику")
    @allure.description("Переход в ЛК пользователя")
    def test_transfer_to_account_on_click(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        current_url = profile_page.check_switch_on_profile()
        assert current_url == URL.PROFILE_URL
    #
    # @allure.title('Тест перехода в "Историю заказов" по клику')
    # @allure.description(
    #     'Переход в "Историю заказов"'
    # )
    # def test_transfer_to_order_history_on_click(self, authorization):
    #     driver = authorization
    #     main_page = MainPage(driver)
    #     main_page.click_personal_account_button()
    #     profile_page = ProfilePage(driver)
    #     profile_page.click_order_history_button()
    #     order_history_page = OrderHistoryPage(driver)
    #     current_url = order_history_page.check_switch_on_order_history()
    #     assert current_url == UrlsConstants.ORDER_HISTORY_URL
    #
    # @allure.title('Тест выхода из аккаунта по клику')
    # @allure.description(
    #     'Выход из профиля по кнопке "Выход"'
    # )
    # def test_account_logout(self, authorization):
    #     driver = authorization
    #     main_page = MainPage(driver)
    #     main_page.click_personal_account_button()
    #     order_history_page = OrderHistoryPage(driver)
    #     order_history_page.click_log_out_button()
    #     login_page = LoginPage(driver)
    #     current_url = login_page.check_switch_on_login_page()
    #     assert current_url == UrlsConstants.LOGIN_URL
