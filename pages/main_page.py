import allure
from locators.main_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Клик на кнопку Личный кабинет")
    def click_personal_account_button(self):
        self.wait_for_clickable_element(MainPageLocators.ACCOUNT_BUTTON)
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step("Тест перехода на главную страницу")
    def check_switch_on_main_page(self):
        self.wait_for_visibility_of_element(MainPageLocators.BURGER_HEADER)
        return self.get_current_url()
