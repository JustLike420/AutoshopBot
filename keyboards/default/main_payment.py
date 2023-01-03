# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from utils.db_api.sqlite import get_paymentx, get_btc


def payment_default():
    payment = get_paymentx()
    btc_payment = get_btc()
    payment_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    # payment_kb.row("🥝 Изменить QIWI 🖍", "🥝 Проверить QIWI ♻", "🥝 Баланс QIWI 👁")
    payment_kb.row("🥝 Добавить QIWI 1", "🥝 Добавить QIWI 2", "Просмотр кошельков", "Удалить кошелек")
    if payment[5] == "True":
        payment_kb.row("🔴 Выключить пополнения")
    else:
        payment_kb.row("🟢 Включить пополнения")
    if btc_payment[2] == "True":
        payment_kb.row("Изменить btc 🖍", "🔴 Выключить пополнения btc")
    else:
        payment_kb.row("Изменить btc 🖍", "🟢 Включить пополнения btc")
    payment_kb.row("Вывод")
    payment_kb.row("⬅ На главную")
    return payment_kb
