from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    PASSWORD_RECOVERY_HEADER = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    EMAIL_FIELD = (By.TAG_NAME, "input")
    RECOVER_BUTTON = (By.XPATH, "'//button[text()='Восстановить']'")
