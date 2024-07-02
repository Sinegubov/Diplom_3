import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage

from data import URL


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Тест перехода на страницу восстановления пароля по кнопке Восстановить пароль")
    @allure.description("Переходим на страницу восстановления пароля и сверяем текущую страницу с константой по URL")
    def test_transfer_to_password_recovery_page(self, password_recovery):
        driver = password_recovery
        forgot_pass_page = ForgotPasswordPage(driver)
        current_url = forgot_pass_page.check_switch_on_forgot_pass()

        assert current_url == URL.FORGOT_PASS_URL

    @allure.title("Тест кнопки Восстановить")
    @allure.description("Ввод почты и клик по кнопке Восстановить")
    def test_recovery_button(self, forgot_pass_page):
        driver = forgot_pass_page
        reset_pass_page = ResetPasswordPage(driver)
        current_url = reset_pass_page.check_transfer_to_reset_password()

        assert current_url == URL.RESET_PASS_URL

    @allure.title("Тест кнопки показать/скрыть пароль")
    @allure.description("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_password_button_and_field_active(self, forgot_pass_page):
        driver = forgot_pass_page
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.set_new_password()
        reset_pass_page.click_show_button()

        assert reset_pass_page.input_field_is_displayed()
