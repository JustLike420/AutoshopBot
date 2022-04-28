# - *- coding: utf- 8 - *-
from aiogram.dispatcher.filters.state import State, StatesGroup


class StorageQiwi(StatesGroup):
    here_input_qiwi_secret = State()
    here_input_qiwi_login = State()
    here_input_qiwi_token = State()
    here_input_qiwi_amount = State()

class StorageYooMoney(StatesGroup):
    client_id = State()
    redirect_uri = State()
    authorize = State()
    here_input_yoo_amount = State()