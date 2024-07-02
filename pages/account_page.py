import allure
from locators.account_locators import AccountLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Проверка перехода на страницу профиля")
    def check_transfer_to_account(self):
        self.wait_for_visibility_of_element(AccountLocators.ACCOUNT_BUTTON)
        return self.get_current_url()

    @allure.step("Нажать на кнопку История заказов")
    def click_order_history_button(self):
        self.wait_for_click_element(AccountLocators.ORDER_HISTORY_BUTTON)
        self.click_element(AccountLocators.ORDER_HISTORY_BUTTON)
