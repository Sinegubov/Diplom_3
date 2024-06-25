from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Личный кабинет"
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    BURGER_HEADER = (By.XPATH, '//h1[text()="Соберите бургер"]')
