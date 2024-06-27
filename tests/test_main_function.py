import allure

from pages.ingredient_page import IngredientPage
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage

from data import URL, Messages


@allure.feature("Проверка основного функционала")
class TestMainFunction:
    @allure.title("Тест перехода по клику на Конструктор")
    @allure.description("Переходим в конструктор и сверяем текущую страницу с константой по URL")
    def test_transfer_to_constructor(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_constructor_button()
        main_page = MainPage(driver)
        current_url = main_page.check_transfer_to_main_page()

        assert current_url == URL.BASE_URL

    @allure.title("Тест перехода по клику на Лента заказов")
    @allure.description("Переходим в Ленту заказов и сверяем текущую страницу с константой по URL")
    def test_transfer_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        current_url = order_feed_page.check_transfer_to_order_feed()

        assert current_url == URL.ORDER_FEED_URL

    @allure.title("Тест появления всплывающего окна с деталями")
    @allure.description("Есл кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_and_show_popup_detail_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_pages = IngredientPage(driver)
        actually_text = ingredient_details_pages.check_window_with_ingredient_details()

        assert actually_text == Messages.INGREDIENT_WINDOW_HEADER

    @allure.title("Тест закрытия всплывающего окна")
    @allure.description("Всплывающее окно закрывается кликом по крестику")
    def test_close_popup_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_pages = IngredientPage(driver)
        ingredient_details_pages.click_close_button()
        displayed = ingredient_details_pages.check_window_with_ingredient_details_closed()

        assert not displayed

    @allure.title("Тест увеличения счётчика ингредиента при добавлении в заказ")
    @allure.description("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_rise_counter_after_adding_ingredient(self, driver):
        main_page = MainPage(driver)
        prev_counter_value = main_page.get_count_value()
        main_page.add_ingredient()
        current_counter_value = main_page.get_count_value()

        assert current_counter_value > prev_counter_value

    @allure.title("Тест оформления заказа залогиненным пользователя")
    @allure.description("Залогиненный пользователь может оформить заказ")
    def test_make_order_by_auth_account(self, auth_user):
        driver = auth_user
        main_page = MainPage(driver)
        main_page.add_ingredient()
        main_page.click_checkout_button()
        actually_text = main_page.get_order_id()

        assert actually_text == Messages.ORDER_ID_MESSAGE
