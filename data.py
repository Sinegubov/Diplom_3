class URL:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    USER_REG_URL = f"{BASE_URL}/api/auth/register"
    USER_DELETE_URL = f"{BASE_URL}/api/auth/user"
    USER_MODIFY_URL = f"{BASE_URL}/api/auth/user"
    ORDER_URL = f"{BASE_URL}/api/orders"
    INGREDIENT_GET_URL = f"{BASE_URL}/api/ingredients"
    LOGIN_URL = f"{BASE_URL}/login"
    ORDER_FEED_URL = f"{BASE_URL}/feed"
    FORGOT_PASS_URL = f"{BASE_URL}/forgot-password"
    RESET_PASS_URL = f"{BASE_URL}/reset-password"
    ORDER_HISTORY_URL = f"{BASE_URL}/account/order-history"
    PROFILE_URL = f"{BASE_URL}/account/profile"


class Messages:
    WINDOW_HEADER = "Детали ингредиента"
    ORDER_ID_MESSAGE = "идентификатор заказа"
