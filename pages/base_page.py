import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание возможности кликнуть на элементе")
    def wait_for_click_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Получить текущую ссылку")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Передать значение элементу")
    def send_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Дождаться видимости элемента")
    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step("Дождаться видимости элемента и вернуть элемент")
    def wait_for_visibility_of_element_and_find(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Дождаться невидимости элемента")
    def wait_for_invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element(locator))

    @allure.step("Найти элемент")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Дождаться появления текста у элемента")
    def wait_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step("Активация сложных действий")
    def action(self):
        return ActionChains(self.driver)

    @allure.step("Смещение перекрывающих окон. Костыль для стабилизации падения тестов на firefox")
    def anti_overlay_click(self):
        self.action().move_by_offset(250, 0).click().perform()

    @allure.step("Отображение элемента")
    def element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Перетаскивание элемента")
    def drag_and_drop_element(self, locator_1, locator_2):
        drag = self.driver.find_element(*locator_1)
        drop = self.driver.find_element(*locator_2)
        self.action().drag_and_drop(drag, drop).perform()
