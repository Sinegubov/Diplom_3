import allure
from locators.main_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Нажать на кнопку Личный кабинет")
    def click_account_button(self):
        self.wait_for_click_element(MainPageLocators.ACCOUNT_BUTTON)
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step("Проверка перехода на главную страницу")
    def check_transfer_to_main_page(self):
        self.wait_for_visibility_of_element(MainPageLocators.BURGER_HEADER)
        return self.get_current_url()

    @allure.step("Нажать на кнопку Лента Заказов")
    def click_order_feed_button(self):
        self.wait_for_click_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Нажать на ингредиент")
    def click_on_ingredient(self):
        self.wait_for_click_element(MainPageLocators.BUN_INGREDIENT)
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Получение значения счетчика ингредиента")
    def get_count_value(self):
        return self.get_text(MainPageLocators.COUNTER)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient(self):
        self.wait_for_visibility_of_element(MainPageLocators.BUN_INGREDIENT)
        self.wait_for_visibility_of_element(MainPageLocators.BASKET)
        self.drag_and_drop_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.BASKET)

    @allure.step("Нажать на кнопку Оформить заказ")
    def click_checkout_button(self):
        self.click_element(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step("Получение ID заказа при оформлении")
    def get_order_id(self):
        self.wait_for_visibility_of_element(MainPageLocators.ORDER_ID)
        return self.get_text(MainPageLocators.ORDER_ID)
