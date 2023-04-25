# - *- coding: utf- 8 - *-
import asyncio
import json

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from pyqiwip2p import QiwiP2P
from filters import IsAdmin
from keyboards.default import payment_default
from keyboards.inline import choice_way_input_payment_func
from loader import dp, bot
from states import StorageCryptopay
from utils import send_all_admin, clear_firstname
from utils.db_api.sqlite import get_paymentx, update_paymentx

from utils import yoomoney_auth, generate_token


###################################################################################
########################### ВКЛЮЧЕНИЕ/ВЫКЛЮЧЕНИЕ ПОПОЛНЕНИЯ #######################
# Включение пополнения
@dp.message_handler(IsAdmin(), text="🔴 Выключить пополнения", state="*")
async def turn_off_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymentx(status="False")
    await message.answer("<b>🔴 Пополнения в боте были выключены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🔴 Выключил пополнения в боте.", not_me=message.from_user.id)


# Выключение пополнения
@dp.message_handler(IsAdmin(), text="🟢 Включить пополнения", state="*")
async def turn_on_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymentx(status="True")
    await message.answer("<b>🟢 Пополнения в боте были включены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🟢 Включил пополнения в боте.", not_me=message.from_user.id)


###################################################################################
############################# ВЫБОР СПОСОБА ПОПОЛНЕНИЯ ############################
# Выбор способа пополнения
@dp.callback_query_handler(IsAdmin(), text_startswith="change_payment:")
async def input_amount(call: CallbackQuery):
    way_pay = call.data[15:]
    change_pass = False
    get_payment = get_paymentx()
    if way_pay == "nickname":
        try:
            request = requests.Session()
            request.headers["authorization"] = "Bearer " + get_payment[1]
            get_nickname = request.get(
                f"https://edge.qiwi.com/qw-nicknames/v1/persons/{get_payment[0]}/nickname")
            check_nickname = json.loads(get_nickname.text).get("nickname")
            if check_nickname is None:
                await call.answer("❗ На аккаунте отсутствует QIWI Никнейм")
            else:
                update_paymentx(qiwi_nickname=check_nickname)
                change_pass = True
        except json.decoder.JSONDecodeError:
            await call.answer("❗ QIWI кошелёк не работает.\n❗ Как можно быстрее установите его",
                              True)
    else:
        change_pass = True
    if change_pass:
        update_paymentx(way_payment=way_pay)
        await bot.edit_message_text("🥝 Выберите способ пополнения 💵\n"
                                    "➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                    "🔸 <a href='https://vk.cc/bYjKGM'><b>По форме</b></a> - <code>Готовая форма оплаты QIWI</code>\n"
                                    "🔸 <a href='https://vk.cc/bYjKEy'><b>По номеру</b></a> - <code>Перевод средств по номеру телефона</code>\n"
                                    "🔸 <a href='https://vk.cc/bYjKJk'><b>По никнейму</b></a> - "
                                    "<code>Перевод средств по никнейму (пользователям придётся вручную вводить комментарий)</code>",
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=choice_way_input_payment_func())


