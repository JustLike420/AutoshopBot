# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from utils.db_api.sqlite import get_paymentx, get_yoomoney, get_crystal


def payment_default():
    payment = get_paymentx()
    payment_y = get_yoomoney()
    payment_c = get_crystal()
    payment_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    payment_kb.row("🥝 Изменить QIWI 🖍", "🥝 Проверить QIWI ♻", "🥝 Баланс QIWI 👁")
    if payment[5] == "True":
        payment_kb.row("🔴 Выключить пополнения qiwi")
    else:
        payment_kb.row("🟢 Включить пополнения qiwi")
    if payment_y[3] == "True":
        payment_kb.row("Изменить YooMoney 🖍", "🔴 Выключить пополнения yoomoney")
    else:
        payment_kb.row("Изменить YooMoney 🖍", "🟢 Включить пополнения yoomoney")
    if payment_c[3] == "True":
        payment_kb.row("Изменить CrystalPay 🖍", "🔴 Выключить пополнения CrystalPay")
    else:
        payment_kb.row("Изменить CrystalPay 🖍", "🟢 Включить пополнения CrystalPay")
    payment_kb.row("⬅ На главную")
    return payment_kb
