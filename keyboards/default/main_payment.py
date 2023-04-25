# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from utils.db_api.sqlite import get_paymentx


def payment_default():
    payment = get_paymentx()
    payment_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    if payment[5] == "True":
        payment_kb.row("🔴 Выключить пополнения")
    else:
        payment_kb.row("🟢 Включить пополнения")
    payment_kb.row("⬅ На главную")
    return payment_kb
