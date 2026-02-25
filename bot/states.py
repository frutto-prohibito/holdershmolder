from aiogram.fsm.state import StatesGroup, State

class OrderState(StatesGroup):
    waiting_for_name = State()
    waiting_for_address = State()
