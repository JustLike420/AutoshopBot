# - *- coding: utf- 8 - *-
import asyncio
import datetime
import time
from aiogram import Dispatcher
from data.config import admins, bot_description
from loader import bot
from utils.db_api.sqlite import get_settingsx, update_settingsx
from requests import post

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

def yoomoney_auth(client_id, redirect_uri):

    data = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': 'account-info operation-history operation-details'
    }

    response = post("http://yoomoney.ru/oauth/authorize", params=data)

    return response.url

def generate_token(client_id, redirect_uri, url):

    url_split = url.split("?")
    auth_code = url_split[1].split("=")[1]

    auth = {
        'code': auth_code,
        'client_id': client_id,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
    }

    response = post("http://yoomoney.ru/oauth/token", params=auth)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None
