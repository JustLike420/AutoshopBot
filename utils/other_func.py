# - *- coding: utf- 8 - *-
import asyncio
import datetime
import time
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
