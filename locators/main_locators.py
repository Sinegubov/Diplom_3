from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUN_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    COUNTER = (By.XPATH, "//ul[1]/a[1]//p[contains(@class, 'num')]")
    BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_ID = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
