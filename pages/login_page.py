import allure
from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Клик на кнопку Восстановить пароль")
    def click_restore_password_button(self):
        self.wait_for_clickable_element(LoginPageLocators.RESTORE_PASSWORD_LINK)
        self.click_element(LoginPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step("Клик на поле email")
    def click_email_field(self):
        self.wait_for_clickable_element(LoginPageLocators.EMAIL)
        self.click_element(LoginPageLocators.EMAIL)

    @allure.step("Заполнение поля email")
    def set_email(self, email):
        self.send_value(LoginPageLocators.EMAIL, email)

    @allure.step("Клик на поле Пароль")
    def click_pass_field(self):
        self.click_element(LoginPageLocators.PASSWORD)

    @allure.step("Заполнение поля Пароль")
    def set_pass(self, password):
        self.send_value(LoginPageLocators.PASSWORD, password)

    @allure.step("Клик на кнопку Войти")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизация")
    def login(self, email, password):
        self.click_email_field()
        self.set_email(email)
        self.click_pass_field()
        self.set_pass(password)
        self.click_login_button()

    @allure.step("Тест перехода на страницу Вход")
    def check_switch_on_login_page(self):
        self.wait_for_visibility_of_element(LoginPageLocators.LOGIN_HEADER)
        return self.get_current_url()
