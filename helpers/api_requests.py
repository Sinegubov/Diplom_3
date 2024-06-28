import requests

from data import URL


class APIRequests:
    @staticmethod
    def get_token(payload):
        response = requests.post(URL.USER_REG_URL, data=payload)
        token = response.json()["accessToken"]
        return token

    @staticmethod
    def get_ingredient():
        response = requests.get(url=URL.INGREDIENT_GET_URL)
        ingredient = response.json()["data"][1]["_id"]

        yield ingredient

    @staticmethod
    def create_order(token):
        ingredient = requests.get(url=URL.INGREDIENT_GET_URL).json()["data"][0]["_id"]
        requests.post(URL.ORDER_URL, headers={"Authorization": token}, data={"ingredients": ingredient})

    @staticmethod
    def get_user_orders(token):
        user_orders = requests.get(URL.ORDER_URL, headers={"Authorization": token}).json()["orders"]
        return user_orders

    @staticmethod
    def delete_user(token):
        requests.delete(URL.AUTH_USER_URL, headers={"Authorization": token})
