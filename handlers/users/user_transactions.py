from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
import asyncio
import requests
import re
import time

from telethon import TelegramClient, events
from data import config
from external.banker import Banker
from external.pycrystalpay import CrystalPay
from keyboards.default import all_back_to_main_default, check_user_out_func
from keyboards.inline import *
from loader import dp, bot
from states.state_payment import StorageQiwi, StorageCrystalPay
from utils import send_all_admin, clear_firstname, get_dates
from utils.db_api.sqlite import update_userx, get_refillx, add_refillx, get_crystal


@dp.callback_query_handler(text="user_input_payment", state="*")
async def input_payment(call: CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="BTCBanker", callback_data="banker_paym"))
    await call.message.answer("<b>Выбери способ оплаты:</b>",
                              reply_markup=markup)


@dp.callback_query_handler(text="banker_paym", state="*")
async def input_banker(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('Пришлите сылку на чек\n'
                              'Если ничего не произошло, пришлите чек повторно через пару секунд')
    await state.set_state("get_banker")


@dp.message_handler(state="get_banker")
async def check_banker(message: types.Message, state: FSMContext):
    link = message.text
    if 'BTC_CHANGE_BOT?start=' in link:
        check_id = re.findall(r"https://telegram\.me/BTC_CHANGE_BOT\?start=(.*)", link)
        banker = Banker(config.api_id, config.api_hash)
        result = await banker.check_cheque(check_id[0])
        if result is not False:
            amount = result
            print(amount)
            add_refillx(message.from_user.id, message.from_user.username, message.from_user.first_name,
                                        link.split('start=')[1],
                                        amount, link.split('start=')[1], 'btc_banker', get_dates(), int(time.time()))
            get_user_info = get_userx(user_id=message.from_user.id)
            # Обновление баланса у пользователя
            update_userx(message.from_user.id,
                         balance=int(get_user_info[4]) + amount,
                         all_refill=int(get_user_info[5]) + amount)

            await message.answer(
                f"<b>✅ Вы успешно пополнили баланс на сумму {amount}руб. Удачи ❤</b>\n"
                f"<b>📃 Чек:</b> <code>+{link.split('start=')[1]}</code>",
                reply_markup=check_user_out_func(message.from_user.id))
            await send_all_admin(f"<b>💰 Пользователь</b> "
                                 f"(@{message.from_user.username}|<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
                                 f"|<code>{message.from_user.id}</code>) "
                                 f"<b>пополнил баланс на сумму</b> <code>{amount}руб</code> 🥝\n"
                                 f"📃 <b>Чек:</b> <code>+{link.split('start=')[1]}</code>")
            await state.finish()
        else:
            await message.answer('Чек невалидный или уже использован')
    else:
        await message.answer('Сылка неверная')

