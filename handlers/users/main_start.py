# - *- coding: utf- 8 - *-
import string

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsWork, IsUser
from filters.all_filters import IsBuy
from keyboards.default import check_user_out_func
from loader import dp, bot
from states import StorageUsers
from utils.db_api.sqlite import *
from utils.other_func import clear_firstname, get_dates, create_captcha

prohibit_buy = ["xbuy_item", "not_buy_items", "buy_this_item", "buy_open_position", "back_buy_item_position",
                "buy_position_prevp", "buy_position_nextp", "buy_category_prevp", "buy_category_nextp",
                "back_buy_item_to_category", "buy_open_category"]


# Проверка на нахождение бота на технических работах
@dp.message_handler(IsWork(), state="*")
@dp.callback_query_handler(IsWork(), state="*")
async def send_work_message(message: types.Message, state: FSMContext):
    if "id" in message:
        await message.answer("🔴 Бот находится на технических работах.")
    else:
        await message.answer("<b>🔴 Бот находится на технических работах.</b>")


@dp.message_handler(text="⬅ На главную", state="*")
@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    first_name = clear_firstname(message.from_user.first_name)
    get_user_id = get_userx(user_id=message.from_user.id)

    if get_user_id is None:
        captcha_text = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
        file_path = create_captcha(captcha_text, message.from_user.id)
        await bot.send_photo(message.chat.id, open(file_path, 'rb'))
        os.remove(file_path)
        await state.update_data(valid_captcha=captcha_text)
        await state.set_state('input_captcha')
    else:
        if first_name != get_user_id[3]:
            update_userx(get_user_id[1], user_name=first_name)
        if message.from_user.username is not None:
            if message.from_user.username.lower() != get_user_id[2]:
                update_userx(get_user_id[1], user_login=message.from_user.username.lower())

        await message.answer("<b>🔸 Бот готов к использованию.</b>\n"
                             "🔸 Если не появились вспомогательные кнопки\n"
                             "▶ Введите /start",
                             reply_markup=check_user_out_func(message.from_user.id))


@dp.message_handler(state="input_captcha")
async def get_captcha(message: types.Message, state: FSMContext):
    captcha = message.text.lower()
    async with state.proxy() as data:
        valid_captcha = data['valid_captcha'].lower()
    if captcha == valid_captcha:
        await message.reply("Капча введена верно")
        await state.finish()
        first_name = clear_firstname(message.from_user.first_name)
        if message.from_user.username is not None:
            get_user_login = get_userx(user_login=message.from_user.username)

            if get_user_login is None:
                add_userx(message.from_user.id, message.from_user.username.lower(), first_name, 0, 0, get_dates())
            else:
                delete_userx(user_login=message.from_user.username)
                add_userx(message.from_user.id, message.from_user.username.lower(), first_name, 0, 0, get_dates())
        else:
            add_userx(message.from_user.id, message.from_user.username, first_name, 0, 0, get_dates())
        await message.answer("<b>🔸 Бот готов к использованию.</b>\n"
                             "🔸 Если не появились вспомогательные кнопки\n"
                             "▶ Введите /start",
                             reply_markup=check_user_out_func(message.from_user.id))

    else:
        await message.reply(f"Капча введена неверно, попробуйте еще раз: {valid_captcha} {captcha}")


@dp.message_handler(IsUser(), state="*")
@dp.callback_query_handler(IsUser(), state="*")
async def send_user_message(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id,
                           "<b>❗ Ваш профиль не был найден.</b>\n"
                           "▶ Введите /start")


# Проверка на доступность покупок
@dp.message_handler(IsBuy(), text="🎁 Купить", state="*")
@dp.message_handler(IsBuy(), state=StorageUsers.here_input_count_buy_item)
@dp.callback_query_handler(IsBuy(), text_startswith=prohibit_buy, state="*")
async def send_user_message(message, state: FSMContext):
    if "id" in message:
        await message.answer("🔴 Покупки в боте временно отключены", True)
    else:
        await message.answer("<b>🔴 Покупки в боте временно отключены</b>")
