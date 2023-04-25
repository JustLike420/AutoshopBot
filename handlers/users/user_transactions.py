# - *- coding: utf- 8 - *-
import json
import random
import time
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink
from pyqiwip2p import QiwiP2P
from aiocryptopay import AioCryptoPay

from data.config import CRYPTO_PAY
from keyboards.default import all_back_to_main_default, check_user_out_func
from keyboards.inline import *
from loader import dp, bot
from states.state_payment import StorageCryptopay
from external.pycrystalpay import CrystalPay
from utils import send_all_admin, clear_firstname, get_dates, get_crypto_bot_sum, \
    check_crypto_bot_invoice
from utils.db_api.sqlite import update_userx, get_refillx, add_refillx, add_payment, get_payment


@dp.callback_query_handler(text="user_input_payment", state="*")
async def input_payment(call: CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="⚜️ CryptoBot", callback_data="cryptobot_paym"))
    await call.message.answer("<b>Выбери способ оплаты:</b>",
                              reply_markup=markup)


###################################################################################
####################################### crypto ###################################
@dp.callback_query_handler(text="cryptobot_paym", state="*")
async def input_amount(call: CallbackQuery, state: FSMContext):
    payment = get_paymentx()
    if payment[5] == "True":
        await StorageCryptopay.sum.set()
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.answer("<b>💵 Введите сумму для пополнения средств</b>",
                                  reply_markup=all_back_to_main_default)

    else:
        await bot.answer_callback_query(call.id, "❗ Пополнение временно недоступно")
        await send_all_admin(
            f"👤 Пользователь <a href='tg://user?id={call.from_user.id}'>{clear_firstname(call.from_user.first_name)}</a> "
            f"пытался пополнить баланс.")


@dp.message_handler(state=StorageCryptopay.sum)
async def crypto_bot_sum(message: types.Message, state: FSMContext):
    try:
        if float(message.text) >= 0.1:
            await message.answer(
                f'— Сумма: <b>{message.text} $</b>\n\n'
                '<b>💸 Выберите валюту, которой хотите оплатить счёт</b>',
                disable_web_page_preview=True,
                reply_markup=crypto_bot_currencies_kb()
            )
            await state.update_data(crypto_bot_sum=float(message.text))
            await StorageCryptopay.currency.set()
        else:
            await message.answer(
                '<b>⚠️ Минимум: 0.1 $!<b>'
            )
    except ValueError:
        await message.answer(
            '<b>❗️Сумма для пополнения должна быть в числовом формате!</b>'
        )


@dp.callback_query_handler(Text(startswith='crypto_bot_currency'), state=StorageCryptopay.currency)
async def crypto_bot_currency(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    cryptopay = AioCryptoPay(CRYPTO_PAY)
    invoice = await cryptopay.create_invoice(
        asset=call.data.split('|')[1],
        amount=await get_crypto_bot_sum(
            data['crypto_bot_sum'],
            call.data.split('|')[1]
        )
    )
    await cryptopay.close()
    add_payment(invoice.invoice_id, data['crypto_bot_sum'])
    await call.message.answer(
        f'<b>💸 Отправьте {data["crypto_bot_sum"]} $ {hlink("по ссылке", invoice.pay_url)}</b>',
        reply_markup=check_crypto_bot_kb(invoice.pay_url, invoice.invoice_id)
    )
    await state.finish()


@dp.callback_query_handler(Text(startswith='check_crypto_bot'), state='*')
async def check_crypto_bot(call: types.CallbackQuery):
    receipt = call.data.split('|')[1]
    payment = get_payment(invoice_id=receipt)

    if payment:
        if await check_crypto_bot_invoice(int(receipt)):
            pay_amount = float(payment[1])
            get_user_info = get_userx(user_id=call.from_user.id)
            get_purchase = get_refillx("*", receipt=receipt)
            if get_purchase is None:
                add_refillx(call.from_user.id, call.from_user.username, call.from_user.first_name,
                            receipt,
                            pay_amount, receipt, 'crypto', get_dates(), int(time.time()))

                update_userx(call.from_user.id,
                             balance=int(get_user_info[4]) + pay_amount,
                             all_refill=int(get_user_info[5]) + pay_amount)

                await call.message.delete()
                await call.message.answer(
                    f"<b>✅ Вы успешно пополнили баланс на сумму {pay_amount}руб. Удачи ❤</b>\n"
                    f"<b>📃 Чек:</b> <code>+{receipt}</code>",
                    reply_markup=check_user_out_func(call.from_user.id))
                await send_all_admin(f"<b>💰 Пользователь</b> "
                                     f"(@{call.from_user.username}|<a href='tg://user?id={call.from_user.id}'>{call.from_user.first_name}</a>"
                                     f"|<code>{call.from_user.id}</code>) "
                                     f"<b>пополнил баланс на сумму</b> <code>{pay_amount}руб</code> 🥝\n"
                                     f"📃 <b>Чек:</b> <code>+{receipt}</code>")
            else:
                await bot.answer_callback_query(call.id, "❗ Ваше пополнение уже зачислено.", True)
            await call.answer(
                '✅ Оплата прошла успешно!',
                show_alert=True
            )
            await call.message.delete()
            await call.message.answer(
                f'<b>💸 Ваш баланс пополнен на сумму {payment.summa} $!</b>'
            )

        else:
            await call.answer(
                '❗️ Вы не оплатили счёт!',
                show_alert=True
            )
