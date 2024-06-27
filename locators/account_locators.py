from selenium.webdriver.common.by import By


class AccountLocators:
    ACCOUNT_BUTTON = (By.LINK_TEXT, 'Профиль')
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, "История заказов")
