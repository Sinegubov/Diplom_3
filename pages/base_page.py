from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_clickable_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def send_value(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_visibility_of_element_and_find(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.text_to_be_present_in_element(locator, text))

    def action(self):
        return ActionChains(self.driver)

    def anti_overlay_click(self):  # чтобы не падали тесты на Firefox
        self.action().move_by_offset(250, 0).click().perform()

    def element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def drag_and_drop_element(self, locator_1, locator_2):
        draggable = self.driver.find_element(*locator_1)
        droppable = self.driver.find_element(*locator_2)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()
