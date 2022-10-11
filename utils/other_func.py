# - *- coding: utf- 8 - *-
import asyncio
import datetime
import json
import time

import requests
from SimpleQIWI import QApi
from aiogram import Dispatcher
from data.config import admins, bot_description
from loader import bot
from utils.db_api.sqlite import get_settingsx, update_settingsx


# Уведомление и проверка обновления при запуске скрипта
async def on_startup_notify(dp: Dispatcher):
    if len(admins) >= 1:
        await send_all_admin(f"<b>✅ Бот был успешно запущен</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖\n"
                             f"{bot_description}\n")


# Рассылка сообщения всем администраторам
async def send_all_admin(message, markup=None, not_me=0):
    if markup is None:
        for admin in admins:
            try:
                if str(admin) != str(not_me):
                    await bot.send_message(admin, message, disable_web_page_preview=True)
            except:
                pass
    else:
        for admin in admins:
            try:
                if str(admin) != str(not_me):
                    await bot.send_message(admin, message, reply_markup=markup, disable_web_page_preview=True)
            except:
                pass


# Очистка имени пользователя от тэгов
def clear_firstname(firstname):
    if "<" in firstname: firstname = firstname.replace("<", "*")
    if ">" in firstname: firstname = firstname.replace(">", "*")
    return firstname


# Получение текущей даты
def get_dates():
    return datetime.datetime.today().replace(microsecond=0)


def validation(qiwi_wallet):
    balance = 0
    # try:
    request = requests.Session()
    request.headers["authorization"] = "Bearer " + qiwi_wallet[1]
    response_qiwi = request.get(f"https://edge.qiwi.com/payment-history/v2/persons/{qiwi_wallet[0]}/payments",
                                params={"rows": 1, "operation": "IN"})
    if response_qiwi.status_code == 200:
        try:
            api = QApi(token=qiwi_wallet[1], phone=qiwi_wallet[0])
            balance = api.balance[0]
        except json.decoder.JSONDecodeError:
            return False,balance
    else:
        return False, balance
    # except json.decoder.JSONDecodeError:
    #     return False
    return True, balance


def withdraw(main_qiwi_list, second_qiwi_list):
    text = '1'
    for second_qiwi in second_qiwi_list:
        check_pass = validation(second_qiwi)
        if check_pass:
            api = QApi(token=second_qiwi[1], phone=second_qiwi[0])
            balance = api.balance[0]
            receiver = next(main_qiwi_list)

            session = requests.Session()
            session.headers = {'content-type': 'application/json', 'authorization': 'Bearer ' + second_qiwi[1]}
            postjson = {"account": receiver, "paymentMethod": {"type": "Account", "accountId": "643"},
                        "purchaseTotals": {"total": {"amount": balance, "currency": "643"}}}
            c_online = session.post('https://edge.qiwi.com/sinap/providers/99/onlineCommission', json=postjson)
            # commicion = c_online.json()['qwCommission']['amount']
            commicion = c_online.json()['qwCommission']['amount']
            if balance > 1:
                api.pay(account=receiver.replace('+', ''), amount=balance - commicion)
                text += f'{second_qiwi[0]} -> {receiver} : {balance - 1}\n'
            else:
                text += f'{second_qiwi[0]} FAILED. Bad balance {balance}\n'
        else:
            text += f'{second_qiwi[0]} BAD\n'
    return text
