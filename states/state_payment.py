# - *- coding: utf- 8 - *-
from aiogram.dispatcher.filters.state import State, StatesGroup


class StorageCryptopay(StatesGroup):
    sum = State()
    currency = State()
