# - *- coding: utf- 8 - *-
from requests import get
from json import loads

__base_url__ = "https://api.crystalpay.ru/v1/"


class CrystalPay:
    """ Управление кассой платежной системы crystal pay

    Данная библиотека позволит Вам встраивать платежную систему crystal pay в Ваш код без особых усилий.

    """

    def __init__(self, login, secret_1):

        """ Функция для  получения данных для работы с кассой.

        Аргументы :
            login - логин кассы.
            secret_1 - первый секретный ключ, требуется для базовых функиця кассы.

        """

        self.crystal_login = login
        self.crystal_secret_1 = secret_1

        self.validate_date()

    def get_balance(self):

        """ Функция для получения баланса кассы.

        Аргументы :
            нет
        Возвращает :
            dict - словарь кошельков и их балансов.

        """

        answer_from_host = loads(get(__base_url__ + '?s={}&n={}&o=balance' \
                                     .format(self.crystal_secret_1, self.crystal_login)).text)

        return answer_from_host['balance']

    def generate_pay_link(self, amount, redirect=None):

        """ Функция генерации ссылки для оплаты.

        Аргументы :
            amount - сумма оплаты
        Возвращает:
            list - id платежа, ссылка для оплаты

        """

        if not redirect:

            answer_from_host = loads(get(__base_url__ + '?s={}' \
                                                        '&n={}&o=receipt-create&amount={}'.format(self.crystal_secret_1,
                                                                                                  self.crystal_login,
                                                                                                  amount)).text)
        else:

            answer_from_host = loads(get(__base_url__ + '?s={}' \
                                                        '&n={}&o=receipt-create&amount={}&redirect={}'.format(
                self.crystal_secret_1,
                self.crystal_login, amount,
                redirect)).text)

        return answer_from_host['id'], answer_from_host['url']

    def validate_date(self):

        """ Функция для проверки данных на правильность.

        Аргументы :
            нет
        Возвращает :
            True - получилось проверить баланс кассы.
            ValueError - не получилось проверить баланс кассы.

        """

        answer_from_host = get(__base_url__ + '?s={}&n={}&o=balance' \
                               .format(self.crystal_secret_1, self.crystal_login, )).text
        if answer_from_host == '{"auth":"error"}':
            raise ValueError('Не получилось зайти в кассу, проверьте данные!')

    def get_pay_status(self, pay_id):

        """ Функция для получения статуса платежа.

        Аргументы :
            pay_id - id платежа
        Возвращает :
            bool - True, если платеж прошел, в ином случае False
            int - сумма платежа

        """

        answer_from_host = loads(get(__base_url__ + f'?s={self.crystal_secret_1}' \
                                                   f'&n={self.crystal_login}&o=receipt-check&i={pay_id}').text)
        if answer_from_host['state'] == 'payed':
            state = True
        else:
            state = False

        return state, answer_from_host['amount']

    def gen_pay_link_by_id(self, pay_id):

        """ Функция для генерации ссылки для оплаты, имея id платежа.

        Аргументы :
            pay_id - id платежа
        Возвращает :
            str - ссылка для оплаты
        """

        return 'https:\/\/pay.crystalpay.ru\/?i={}'.format(pay_id)
