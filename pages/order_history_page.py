import allure
from locators.order_history_locators import OrderHistoryLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    @allure.step("Проверка перехода на страницу История заказов")
    def check_transfer_to_order_history(self):
        self.wait_for_visibility_of_element(OrderHistoryLocators.ON_ORDER_HISTORY_BUTTON)
        return self.get_current_url()

    @allure.step("Дождаться и нажать на кнопку Выход")
    def click_log_out_button(self):
        self.wait_for_click_element(OrderHistoryLocators.EXIT_BUTTON)
        self.click_element(OrderHistoryLocators.EXIT_BUTTON)
