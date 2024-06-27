import allure
from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Проверка перехода на страницу восстановления пароля по кнопке Восстановить пароль")
    def check_switch_on_forgot_pass(self):
        self.wait_for_visibility_of_element(ForgotPasswordLocators.PASSWORD_RECOVERY_HEADER)
        return self.get_current_url()

    @allure.step("Заполнить поле Email")
    def fill_email_field(self, email):
        self.wait_for_clickable_element(ForgotPasswordLocators.EMAIL_FIELD)
        self.click_element(ForgotPasswordLocators.EMAIL_FIELD)
        self.send_value(ForgotPasswordLocators.EMAIL_FIELD, email)

    @allure.step("Нажать на кнопу Восстановить")
    def click_recover_button(self):
        self.click_element(ForgotPasswordLocators.RECOVER_BUTTON)
