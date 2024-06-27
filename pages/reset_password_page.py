import allure
from locators.reset_password_locators import ResetPasswordLocators
from helpers.data_generator import UserGenerator
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Тест перехода на страницу сброса пароля")
    def check_switch_on_reset_pass(self):
        self.anti_overlay_click()
        self.wait_for_clickable_element(ResetPasswordLocators.RESET_CODE_FILED)
        return self.get_current_url()

    @allure.step("Ввести новый пароль")
    def set_new_password(self, password=UserGenerator().generate_user_password()):
        self.wait_for_visibility_of_element_and_find(ResetPasswordLocators.FIELD_NEW_PASSWORD).send_keys(password)

    @allure.step("Клик на кнопку «Показать пароль»")
    def click_show_button(self):
        self.wait_for_visibility_of_element(ResetPasswordLocators.SHOW_BUTTON)
        self.anti_overlay_click()
        self.click_element(ResetPasswordLocators.SHOW_BUTTON)

    def input_field_is_displayed(self):
        return self.element_displayed(ResetPasswordLocators.INPUT_ACTIVE)

    @allure.step("Тест, что поле «пароль» стало активным")
    def check_pass_field_active(self):
        return self.get_attribute(ResetPasswordLocators.PASSWORD_FIELD, "name")
