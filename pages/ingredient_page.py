import allure

from locators.ingredient_locators import IngredientDetailsLocators

from pages.base_page import BasePage


class IngredientPage(BasePage):
    @allure.step("Ожидание появления всплывающего окна с деталями")
    def check_window_with_ingredient_details(self):
        self.wait_for_visibility_of_element(IngredientDetailsLocators.DETAILS_HEADER)
        return self.get_text(IngredientDetailsLocators.DETAILS_HEADER)

    @allure.step("Закрыть")
    def click_close_button(self):
        self.click_element(IngredientDetailsLocators.CLOSE_BUTTON)

    @allure.step("Ожидание закрытия всплывающего окна")
    def check_window_with_ingredient_details_closed(self):
        self.wait_for_invisibility_of_element(IngredientDetailsLocators.DETAILS_HEADER)
        return self.element_displayed(IngredientDetailsLocators.DETAILS_HEADER)
