# - *- coding: utf- 8 - *-
import hashlib
import urllib
from requests import get, post
from json import loads

__base_url__ = "https://payok.io"


class PayOk:
    """ Управление кассой платежной системы payok

    Данная библиотека позволит Вам встраивать платежную систему payok в Ваш код без особых усилий.

    """

    def __init__(self, API_ID, API_KEY, secret, shop):

        """ Функция для  получения данных для работы с кассой.

        Аргументы :
            API_ID -
            API_KEY -
            secret -
            shop -

        """

        self.API_ID = API_ID
        self.API_KEY = API_KEY
        self.secret = secret
        self.shop = shop

    def get_balance(self):

        """ Функция для получения баланса кассы.

        Аргументы :
            нет
        Возвращает :
            float - сумма

        """
        data = {
            'API_ID': self.API_ID,
            'API_KEY': self.API_KEY
        }
        answer_from_host = loads(post(__base_url__ + '/api/balance', data).text)

        return answer_from_host['balance']

    def generate_pay_link(self, amount, comment):

        """ Функция генерации ссылки для оплаты.

        Аргументы :
            amount - сумма оплаты
        Возвращает:
            str - ссылка для оплаты

        """

        data = {
            'amount': amount,
            'payment': comment,
            'shop': self.shop,
            'desc': 'desc',
            'currency': 'RUB',
            'method': 'card',
            'custom': 'test'
        }
        sign_str = "|".join(map(str, (
            data["amount"], data["payment"], data["shop"], data["currency"], data["desc"], self.secret)))
        data["sign"] = hashlib.md5(sign_str.encode()).hexdigest()
        # answer_from_host = post(__base_url__ + '/pay', data)
        answer_from_host = __base_url__ + '/pay' + "?" + urllib.parse.urlencode(data)
        return answer_from_host

    def get_pay_status(self, pay_id):

        """ Функция для получения статуса платежа.

        Аргументы :
            pay_id - id платежа
        Возвращает :
            bool - True, если платеж прошел, в ином случае False
            float - сумма платежа

        """

        data = {
            'API_ID': self.API_ID,
            'API_KEY': self.API_KEY,
            'shop': self.shop,
            'payment': pay_id
        }
        answer_from_host = loads(post(__base_url__ + '/api/transaction', data).text)
        print(answer_from_host)
        amount = -1
        if answer_from_host['status'] == 'error':
            state = False
        elif answer_from_host['1']['transaction_status'] == '1':
            state = True
            amount = float(answer_from_host['1']['amount_profit'])
        else:
            state = False
        return state, amount


def del_tab(x: str):
    print(x)

