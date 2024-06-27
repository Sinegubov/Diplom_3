import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Тест перехода на страницу профиля")
    def check_switch_on_profile(self):
        self.wait_for_visibility_of_element(ProfilePageLocators.PROFILE_BUTTON)
        return self.get_current_url()

    @allure.step("Клик на кнопку «История заказов»")
    def click_order_history_button(self):
        self.wait_for_clickable_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)
        self.click_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)
