import requests


class BitcoinPay:
    def __init__(self, rub_amount: int, btc_amount: float = None, address: str = None) -> object:
        self._address = address
        self.btc_rate = None
        self.rub_amount = rub_amount
        if btc_amount:
            self.amount_to_pay = btc_amount
        else:
            self.amount_to_pay = None

    def get_address(self) -> str:
        return self._address

    def get_rate(self):
        """получение курса криптовалюты"""
        url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCRUB'
        rate = requests.get(url).json()['price']
        self.btc_rate = float(rate)

    def get_amount_to_pay(self):
        """получение кол-во биткоинов для оплаты с учетом сатоши"""
        btc_amount = self.rub_amount / self.btc_rate
        btc_amount = round(btc_amount, 8)
        self.amount_to_pay = btc_amount

    def get_trans(self):
        """получение всех транзакций кошелька"""
        url = f'https://chain.api.btc.com/v3/address/{self._address}/tx'
        data = requests.get(url).json()
        return data

    @staticmethod
    def get_satoshi(amount: float) -> int:
        """получение из суммы сатоши"""
        amount = int(format(amount * 10**8, '.0f'))
        return amount

# пример
# def create_order():
#     rub = 500
#     b = BitcoinPay(rub)
#     b.get_rate()
#     b.get_amount_to_pay()
#     pay_btc = b.amount_to_pay
#     print(rub, pay_btc)

# def check_order():
#     rub = 500
#     btc = 0.00048283
#     time_start = 1669331109
#     b = BitcoinPay(rub, btc)
#     data = b.get_trans()
#
#     for tx in data['list']:
#         confirmations = tx['confirmations']
#         block_time = tx['block_time'] + 3 * 3600
#
#         # print(confirmations, block_time)
#         if block_time >= time_start:
#             for out in tx['outputs']:
#
#                 if out['addresses'][0] == b.get_address() and out['value'] == b.get_satoshi(btc):
#                     print(True)

