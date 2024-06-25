import allure
from pages.forgot_password_page import ForgotPasswordPage
from data import URL


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description(
        'Переход на страницу восстановления пароля'
    )
    def test_transfer_to_page_password_recovery(self, password_recovery):
        driver = password_recovery
        forgot_pass_page = ForgotPasswordPage(driver)
        current_url = forgot_pass_page.check_switch_on_forgot_pass()
        assert current_url == URL.FORGOT_PASS_URL
