# - *- coding: utf- 8 - *-
import asyncio
import json
from itertools import cycle

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from pyqiwip2p import QiwiP2P

from filters import IsAdmin
from keyboards.default import payment_default
from keyboards.inline import choice_way_input_payment_func
from loader import dp, bot
from states import StorageQiwi
from utils import send_all_admin, clear_firstname
from utils.db_api.sqlite import get_paymentx, update_paymentx, add_qiwi_payment, get_qiwi_paymentx, delete_qiwi_wallet
from utils.other_func import validation, withdraw


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
            get_nickname = request.get(f"https://edge.qiwi.com/qw-nicknames/v1/persons/{get_payment[0]}/nickname")
            check_nickname = json.loads(get_nickname.text).get("nickname")
            if check_nickname is None:
                await call.answer("❗ На аккаунте отсутствует QIWI Никнейм")
            else:
                update_paymentx(qiwi_nickname=check_nickname)
                change_pass = True
        except json.decoder.JSONDecodeError:
            await call.answer("❗ QIWI кошелёк не работает.\n❗ Как можно быстрее установите его", True)
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


###################################################################################
####################################### QIWI ######################################
# Изменение QIWI кошелька
@dp.message_handler(IsAdmin(), text="🥝 Добавить QIWI 2", state="*")
async def change_qiwi_login(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>🥝 Введите</b> <code>логин(номер)</code> <b>QIWI кошелька 2️⃣</b>")
    await StorageQiwi.here_input_qiwi_login.set()

@dp.message_handler(IsAdmin(), text="🥝 Добавить QIWI 1", state="*")
async def change_qiwi_login1(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>🥝 Введите</b> <code>логин(номер)</code> <b>QIWI кошелька 1️</b>")
    await state.set_state("here_qiwi1_input")


@dp.message_handler(IsAdmin(), state="here_qiwi1_input")
async def change_qiwi__login1(message: types.Message, state: FSMContext):
    number = str(message.text)
    await message.answer(f"QIWI кошелька 1️ {number} добавлен")
    add_qiwi_payment(qiwi_login=number, qiwi_token='',
                     qiwi_private_key='', type='1')
    await state.finish()
# Проверка работоспособности QIWI
@dp.message_handler(IsAdmin(), text="🥝 Проверить QIWI ♻", state="*")
async def check_qiwi(message: types.Message, state: FSMContext):
    await state.finish()
    get_payments = get_paymentx()
    check_pass = True
    if get_payments[0] != "None" or get_payments[1] != "None" or get_payments[2] != "None":
        try:
            request = requests.Session()
            request.headers["authorization"] = "Bearer " + get_payments[1]
            response_qiwi = request.get(f"https://edge.qiwi.com/payment-history/v2/persons/{get_payments[0]}/payments",
                                        params={"rows": 1, "operation": "IN"})
            if response_qiwi.status_code == 200:
                try:
                    qiwi = QiwiP2P(get_payments[2])
                    bill = qiwi.bill(amount=1, lifetime=1)
                except json.decoder.JSONDecodeError:
                    check_pass = False
            else:
                check_pass = False
        except json.decoder.JSONDecodeError:
            check_pass = False
        if check_pass:
            await message.answer(f"<b>🥝 QIWI кошелёк полностью функционирует ✅</b>\n"
                                 f"👤 Логин: <code>{get_payments[0]}</code>\n"
                                 f"♻ Токен: <code>{get_payments[1]}</code>\n"
                                 f"📍 Приватный ключ: <code>{get_payments[2]}</code>")
        else:
            await message.answer("<b>🥝 QIWI кошелёк не прошёл проверку ❌</b>\n"
                                 "❗ Как можно быстрее его замените ❗")
    else:
        await message.answer("<b>🥝 QIWI кошелёк отсутствует ❌</b>\n"
                             "❗ Как можно быстрее его установите ❗")


# Обработка кнопки "Баланс Qiwi"
@dp.message_handler(IsAdmin(), text="🥝 Баланс QIWI 👁", state="*")
async def balance_qiwi(message: types.Message, state: FSMContext):
    await state.finish()
    get_payments = get_paymentx()
    if get_payments[0] != "None" or get_payments[1] != "None" or get_payments[2] != "None":
        request = requests.Session()
        request.headers["authorization"] = "Bearer " + get_payments[1]
        response_qiwi = request.get(f"https://edge.qiwi.com/funding-sources/v2/persons/{get_payments[0]}/accounts")
        if response_qiwi.status_code == 200:
            get_balance = response_qiwi.json()["accounts"][0]["balance"]["amount"]
            await message.answer(
                f"<b>🥝 Баланс QIWI кошелька</b> <code>{get_payments[0]}</code> <b>составляет:</b> <code>{get_balance} руб</code>")
        else:
            await message.answer("<b>🥝 QIWI кошелёк не работает ❌</b>\n"
                                 "❗ Как можно быстрее его замените ❗")
    else:
        await message.answer("<b>🥝 QIWI кошелёк отсутствует ❌</b>\n"
                             "❗ Как можно быстрее его установите ❗")


# Принятие логина для киви
@dp.message_handler(IsAdmin(), state=StorageQiwi.here_input_qiwi_login)
async def change_key_api(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["here_input_qiwi_login"] = message.text
    await message.answer("<b>🥝 Введите</b> <code>токен API</code> <b>QIWI кошелька 🖍</b>\n"
                         "❕ Получить можно тут 👉 <a href='https://qiwi.com/api'><b>Нажми на меня</b></a>\n"
                         "❕ При получении токена, ставьте только первые 3 галочки.",
                         disable_web_page_preview=True)
    await StorageQiwi.here_input_qiwi_token.set()


# Принятие токена для киви
@dp.message_handler(IsAdmin(), state=StorageQiwi.here_input_qiwi_token)
async def change_secret_api(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["here_input_qiwi_token"] = message.text
    await message.answer("<b>🥝 Введите</b> <code>Секретный ключ 🖍</code>\n"
                         "❕ Получить можно тут 👉 <a href='https://qiwi.com/p2p-admin/transfers/api'><b>Нажми на меня</b></a>",
                         disable_web_page_preview=True)
    await StorageQiwi.here_input_qiwi_secret.set()


# Принятие приватного ключа для киви
# @dp.message_handler(IsAdmin(), state=StorageQiwi.here_input_qiwi_secret)
# async def change_secret_api(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["here_input_qiwi_secret"] = message.text
#     await message.answer("Выберите тип qiwi:\n"
#                          "<b>1 - Основной(вывод)</b>\n"
#                          "<b>2 - Второстепенный(прием)</b>\n"
#                          "Напишите цифру.",
#                          disable_web_page_preview=True)
#     await StorageQiwi.here_input_qiwi_type.set()


@dp.message_handler(IsAdmin(), state=StorageQiwi.here_input_qiwi_secret)
async def change_secret_api(message: types.Message, state: FSMContext):
    qiwi_private_key = message.text
    secrey_key_error = False
    async with state.proxy() as data:
        qiwi_login = data["here_input_qiwi_login"]
        qiwi_token = data["here_input_qiwi_token"]
    delete_msg = await message.answer("<b>🥝 Проверка введённых QIWI данных... 🔄</b>")
    await asyncio.sleep(0.5)
    try:
        qiwi = QiwiP2P(qiwi_private_key)
        bill = qiwi.bill(amount=1, lifetime=1)
        try:
            request = requests.Session()
            request.headers["authorization"] = "Bearer " + qiwi_token
            check_history = request.get(f"https://edge.qiwi.com/payment-history/v2/persons/{qiwi_login}/payments",
                                        params={"rows": 1, "operation": "IN"})
            check_profile = request.get(
                f"https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true")
            check_balance = request.get(f"https://edge.qiwi.com/funding-sources/v2/persons/{qiwi_login}/accounts")
            try:
                if check_history.status_code == 200 and check_profile.status_code == 200 and check_balance.status_code == 200:

                    # update_paymentx(qiwi_login=qiwi_login, qiwi_token=qiwi_token,
                    #                 qiwi_private_key=qiwi_private_key)
                    add_qiwi_payment(qiwi_login=qiwi_login, qiwi_token=qiwi_token,
                                     qiwi_private_key=qiwi_private_key, type='2')
                    await delete_msg.delete()
                    await message.answer("<b>🥝 Основной QIWI был успешно добавлен ✅</b>",
                                         reply_markup=payment_default())
                    payments = get_paymentx()
                    if payments[0] == 'None':
                        update_paymentx(qiwi_login=qiwi_login, qiwi_token=qiwi_token,
                                        qiwi_private_key=qiwi_private_key, type='2')

                elif check_history.status_code == 400 or check_profile.status_code == 400 or check_balance.status_code == 400:
                    await delete_msg.delete()
                    await message.answer(f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Код ошибки: Номер телефона указан в неверном формате</code>",
                                         reply_markup=payment_default())
                elif check_history.status_code == 401 or check_profile.status_code == 401 or check_balance.status_code == 401:
                    await delete_msg.delete()
                    await message.answer(f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Код ошибки: Неверный токен или истек срок действия токена API</code>",
                                         reply_markup=payment_default())
                elif check_history.status_code == 403 or check_profile.status_code == 403 or check_balance.status_code == 403:
                    await delete_msg.delete()
                    await message.answer(f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Ошибка: Нет прав на данный запрос (недостаточно разрешений у токена API)</code>",
                                         reply_markup=payment_default())
                else:
                    if check_history.status_code != 200:
                        status_coude = check_history.status_code
                    elif check_profile.status_code != 200:
                        status_coude = check_profile.status_code
                    elif check_balance.status_code != 200:
                        status_coude = check_balance.status_code
                    await delete_msg.delete()
                    await message.answer(f"<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                         f"<code>▶ Код ошибки: {status_coude}</code>",
                                         reply_markup=payment_default())
            except json.decoder.JSONDecodeError:
                await delete_msg.delete()
                await message.answer("<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                     "<code>▶ Токен не был найден</code>",
                                     reply_markup=payment_default())
        except IndexError:
            await delete_msg.delete()
            await message.answer("<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                 "<code>▶ IndexError</code>",
                                 reply_markup=payment_default())
        except UnicodeEncodeError:
            await delete_msg.delete()
            await message.answer("<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                                 "<code>▶ Токен не был найден</code>",
                                 reply_markup=payment_default())
    except json.decoder.JSONDecodeError:
        secrey_key_error = True
    except UnicodeEncodeError:
        secrey_key_error = True
    except ValueError:
        secrey_key_error = True
    except FileNotFoundError:
        secrey_key_error = True
    if secrey_key_error:
        await delete_msg.delete()
        await message.answer("<b>🥝 Введённые QIWI данные не прошли проверку ❌</b>\n"
                             "<code>▶ Неверный приватный ключ</code>\n"
                             "<u>❗ Указывайте СЕКРЕТНЫЙ КЛЮЧ, а не публичный</u>\n"
                             "❕ Секретный ключ заканчивается на =",
                             reply_markup=payment_default())
    await state.finish()


@dp.message_handler(IsAdmin(), text="Просмотр кошельков", state="*")
async def check_wallets(message: types.Message, state: FSMContext):
    await state.finish()
    all_qiwi = get_qiwi_paymentx()
    print(all_qiwi)
    text = ''
    for qiwi_wallet in all_qiwi:
        check, balance = validation(qiwi_wallet)
        if qiwi_wallet[3] == '1':
            wallet_text = '1️⃣ ' + qiwi_wallet[0] + f' {balance}₽ '
        else:
            wallet_text = '2️⃣ ' + qiwi_wallet[0] + f' {balance}₽ '
        if check:
            text += wallet_text + ' ✅\n'
        else:
            text += wallet_text + ' ❌\n'
    await message.answer(text,
                         reply_markup=payment_default())


@dp.message_handler(IsAdmin(), text="Вывод", state="*")
async def withdraw_balance(message: types.Message, state: FSMContext):
    await state.finish()
    all_qiwi = get_qiwi_paymentx()
    main_qiwi_list = [wallet[0] for wallet in all_qiwi if wallet[3] == '1']
    second_qiwi_list = [(wallet[0], wallet[1]) for wallet in all_qiwi if wallet[3] == '2']
    if len(main_qiwi_list) == 0:
        await message.answer("Не хватает основного кошелька")
    elif len(second_qiwi_list) == 0:
        await message.answer("Не хватает второстепенного кошелька")
    else:
        text = withdraw(cycle(main_qiwi_list), second_qiwi_list)
        await message.answer(text)


@dp.message_handler(IsAdmin(), text="Удалить кошелек", state="*")
async def delete_wallet(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>🥝 Введите</b> <code>логин(номер)</code> <b>QIWI кошелька🖍 </b>")
    await state.set_state("delete_wallet")


@dp.message_handler(IsAdmin(), state="delete_wallet")
async def change_key_api(message: types.Message, state: FSMContext):
    wallet_login = str(message.text)
    delete_qiwi_wallet(qiwi_login=wallet_login)
    await message.answer(f"{wallet_login} Удален.")
