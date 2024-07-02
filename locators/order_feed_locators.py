from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]")
    POP_UP_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_order')]")
    ORDER_NUMBERS = (By.XPATH, "//p[@class='text text_type_digits-default']")
    LAST_ORDER = (By.XPATH, "//li[1]//p[@class='text text_type_digits-default']")
    BIG_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/../p[contains(@class, 'digits')]")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'digits')]")
    NUMBER_IN_PROGRESS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li")
