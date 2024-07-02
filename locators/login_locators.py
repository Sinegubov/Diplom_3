from selenium.webdriver.common.by import By


class LoginPageLocators:
    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    EMAIL = (By.NAME, "name")
    PASSWORD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[(text()='Войти')]")
    LOGIN_HEADER = (By.XPATH, ".// h2[text() = 'Вход']")
