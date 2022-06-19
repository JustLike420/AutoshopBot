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
from states import StorageQiwi, StorageYooMoney, StorageCrystalPay
from utils import send_all_admin, clear_firstname
from utils.db_api.sqlite import get_paymentx, update_paymentx, edit_yoomoney, update_paymenty, update_paymentc, edit_crystal

from utils import yoomoney_auth, generate_token


###################################################################################
########################### ВКЛЮЧЕНИЕ/ВЫКЛЮЧЕНИЕ ПОПОЛНЕНИЯ #######################
# Включение пополнения
@dp.message_handler(IsAdmin(), text="🔴 Выключить пополнения qiwi", state="*")
async def turn_off_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymentx(status="False")
    await message.answer("<b>🔴 Пополнения qiwi в боте были выключены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🔴 Выключил пополнения  qiwi в боте.", not_me=message.from_user.id)


# Выключение пополнения
@dp.message_handler(IsAdmin(), text="🟢 Включить пополнения qiwi", state="*")
async def turn_on_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymentx(status="True")
    await message.answer("<b>🟢 Пополнения qiwi в боте были включены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🟢 Включил пополнения qiwi в боте.", not_me=message.from_user.id)


# Включение пополнения
@dp.message_handler(IsAdmin(), text="🔴 Выключить пополнения yoomoney", state="*")
async def turn_off_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymenty(status="False")
    await message.answer("<b>🔴 Пополнения yoomoney в боте были выключены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🔴 Выключил пополнения yoomoney в боте.", not_me=message.from_user.id)


# Выключение пополнения
@dp.message_handler(IsAdmin(), text="🟢 Включить пополнения yoomoney", state="*")
async def turn_on_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymenty(status="True")
    await message.answer("<b>🟢 Пополнения yoomoney в боте были включены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🟢 Включил пополнения yoomoney в боте.", not_me=message.from_user.id)

@dp.message_handler(IsAdmin(), text="🔴 Выключить пополнения CrystalPay", state="*")
async def turn_off_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymentc(status="False")
    await message.answer("<b>🔴 Пополнения CrystalPay в боте были выключены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🔴 Выключил пополнения yoomoney в боте.", not_me=message.from_user.id)


# Выключение пополнения
@dp.message_handler(IsAdmin(), text="🟢 Включить пополнения CrystalPay", state="*")
async def turn_on_refill(message: types.Message, state: FSMContext):
    await state.finish()
    update_paymentc(status="True")
    await message.answer("<b>🟢 Пополнения CrystalPay в боте были включены.</b>",
                         reply_markup=payment_default())
    await send_all_admin(
        f"👤 Администратор <a href='tg://user?id={message.from_user.id}'>{clear_firstname(message.from_user.first_name)}</a>\n"
        "🟢 Включил пополнения yoomoney в боте.", not_me=message.from_user.id)


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
@dp.message_handler(IsAdmin(), text="🥝 Изменить QIWI 🖍", state="*")
async def change_qiwi_login(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("<b>🥝 Введите</b> <code>логин(номер)</code> <b>QIWI кошелька🖍 </b>")
    await StorageQiwi.here_input_qiwi_login.set()


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
@dp.message_handler(IsAdmin(), state=StorageQiwi.here_input_qiwi_secret)
async def change_secret_api(message: types.Message, state: FSMContext):
    secrey_key_error = False
    async with state.proxy() as data:
        qiwi_login = data["here_input_qiwi_login"]
        qiwi_token = data["here_input_qiwi_token"]
    qiwi_private_key = message.text
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
                    update_paymentx(qiwi_login=qiwi_login, qiwi_token=qiwi_token,
                                    qiwi_private_key=qiwi_private_key)
                    await delete_msg.delete()
                    await message.answer("<b>🥝 QIWI токен был успешно изменён ✅</b>",
                                         reply_markup=payment_default())
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


###################################################################################
####################################### YOOMONEY ##################################

@dp.message_handler(IsAdmin(), text="Изменить YooMoney 🖍", state="*")
async def client_id(message: types.Message):
    await message.answer("Зарегестрируйте API <a href='https://yoomoney.ru/myservices/new'>здесь</a>\n"
                         "📱 Введите <b>client_id</b>")
    await StorageYooMoney.client_id.set()


@dp.message_handler(state=StorageYooMoney.client_id)
async def redirect_uri(message: types.Message, state: FSMContext):
    id = message.text

    await state.update_data(client_id=id)
    await StorageYooMoney.next()
    await message.answer("🌐 Введите <b>redirect_uri</b>")


@dp.message_handler(state=StorageYooMoney.redirect_uri)
async def authorize_url(message: types.Message, state: FSMContext):
    uri = message.text

    await state.update_data(redirect_uri=uri)
    data = await state.get_data()

    auth_url = yoomoney_auth(data['client_id'], uri)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="💻 Активация", url=auth_url))

    await message.answer("❗️ Перейдите по ссылке, подтвердите данные и скопируйте полученную ссылку после "
                         "переадресации\n "
                         "❗️ Время действия полученной ссылки <b>1 минута</b>",
                         reply_markup=keyboard)
    await StorageYooMoney.next()


@dp.message_handler(state=StorageYooMoney.authorize)
async def authorize_payment(message: types.Message, state: FSMContext):
    url = message.text

    data = await state.get_data()

    access_token = generate_token(data['client_id'], data['redirect_uri'], url)

    if access_token is not None:
        # токен получен успешно
        num = access_token.split(".")[0]
        await state.update_data(num=num)
        await state.update_data(token=access_token)

        yoomoney_data = await state.get_data()
        edit_yoomoney(yoomoney_data)

        message_text = "✅ Кошелек изменен"
    else:
        message_text = "❗️ Кошелек не доступен, повторите добавление снова"
    await message.answer(message_text)
    # await message.answer(message_text, reply_markup=get_keyboard_for_finish(message.chat.id))

    await state.finish()

###################################################################################
####################################### CRYSTAL PAY ##################################

@dp.message_handler(IsAdmin(), text="Изменить CrystalPay 🖍", state="*")
async def client_id(message: types.Message):
    await message.answer(""
                         "Введите <b>название</b>")
    await StorageCrystalPay.name.set()


@dp.message_handler(state=StorageCrystalPay.name)
async def name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(name=name)
    await StorageCrystalPay.next()
    await message.answer("🌐 Введите <b>secret token</b>")


@dp.message_handler(state=StorageCrystalPay.secret)
async def secret(message: types.Message, state: FSMContext):
    secret = message.text

    await state.update_data(secret=secret)

    crystal_data = await state.get_data()
    edit_crystal(crystal_data)
    await message.answer('✅ Кошелек изменен')
    await state.finish()


