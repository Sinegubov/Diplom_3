from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    PASSWORD_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'")
    FIELD_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_BUTTON = (By. XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    RESET_CODE_FILED = (By.XPATH,  "//label[text()='Введите код из письма']")
    INPUT_ACTIVE = (By.XPATH,  "//div[contains(@class, 'input') and contains (@class, 'input_status_active')]")
