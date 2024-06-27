import allure
import requests

from locators.order_feed_locators import OrderFeedLocators
from helpers.api_requests import APIRequests
from pages.base_page import BasePage
from data import URL


class OrderFeedPage(BasePage):
    @allure.step("Проверка перехода на страницу Лента заказов")
    def check_transfer_to_order_feed(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER)
        return self.get_current_url()

    @allure.step("Клик на кнопку Конструктор")
    def click_constructor_button(self):
        self.click_element(OrderFeedLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на заказ")
    def click_on_order(self):
        self.wait_for_click_element(URL.ORDER_URL)
        self.click_element(OrderFeedLocators.ORDER)

    @allure.step("Проверка появление всплывающего окна с деталями")
    def check_show_window_with_details(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.POP_UP_WINDOW)
        return self.element_displayed(OrderFeedLocators.POP_UP_WINDOW)

    @allure.step("Получение номеров всех заказов в Ленте заказов")
    def get_numbers_of_all_orders(self, user_orders):
        last_order = '0' + str(user_orders[-1])
        self.wait_text_in_element(OrderFeedLocators.NUMBER_IN_PROGRESS, last_order)
        text = '#0' + str(user_orders[-1])
        self.wait_text_in_element(OrderFeedLocators.LAST_ORDER, text)
        all_elements = self.find_elements(OrderFeedLocators.ORDER_NUMBERS)
        return [element.text.strip('#0') for element in all_elements]

    @allure.step("Получение значения счетчика заказов")
    def get_order_counter(self, counter):
        self.wait_for_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER)
        return self.get_text(counter)

    @allure.step("Создание нового заказа")
    def create_order(self, user_token):
        token = user_token
        payload = APIRequests.get_ingredient()
        requests.post(URL.ORDER_URL, headers={"Authorization": token}, data=payload)

    @allure.step("Получение номера заказа")
    def get_user_order_number(self, orders_numbers):
        last_order = '0' + str(orders_numbers[-1])
        self.wait_text_in_element(OrderFeedLocators.NUMBER_IN_PROGRESS, last_order)
        return last_order

    @allure.step("Получение номера заказа В работе")
    def get_user_order_in_progress(self):
        return self.get_text(OrderFeedLocators.NUMBER_IN_PROGRESS)
