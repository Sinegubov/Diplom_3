import requests

from data import URL


class APIRequests:
    @staticmethod
    def get_token(payload):
        token = requests.post(URL.USER_REG_URL, data=payload).json()['accessToken']
        return token

    @staticmethod
    def create_order(token):
        response = requests.get(url=URL.INGREDIENT_GET_URL)
        ingredient = response.json()["data"][1]["_id"]
        requests.post(URL.ORDER_URL, headers={'Authorization': token}, data=ingredient)

    @staticmethod
    def get_user_orders(token):
        user_orders = requests.get(URL.ORDER_URL, headers={'Authorization': token}).json()["orders"]
        return user_orders

    @staticmethod
    def delete_user(token):
        requests.delete(URL.USER_DELETE_URL, headers={'Authorization': token})
