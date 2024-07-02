from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    EXIT_BUTTON = (By.XPATH, "//button[(text()='Выход')]")
    ON_ORDER_HISTORY_BUTTON = (By.XPATH, "//ul/li[2]/a[contains(@class, 'Account_link_active')]")
