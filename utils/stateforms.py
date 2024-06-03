from aiogram.fsm.state import StatesGroup, State
from handlers import bot_messages

class StepsForm(StatesGroup):
    GET_FIO = State()
    GET_CHEH = State()
    GET_PODRASDELENIE = State()
    GET_ULUCHENIE = State()
    GET_PREDLOSHENIE = State()
    GET_PROBLEMA = State()
    GET_PHOTO_1 = State()
    GET_RESHENIE = State()
    GET_PHOTO_2 = State()
    GET_vibor = State()