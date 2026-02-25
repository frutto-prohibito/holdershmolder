from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()


class OrderState(StatesGroup):
    waiting_for_name = State()
    waiting_for_address = State()


@router.message()
async def start_order(message: Message, state: FSMContext):
    await message.answer("Введите ваше имя:")
    await state.set_state(OrderState.waiting_for_name)


@router.message(OrderState.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите адрес доставки:")
    await state.set_state(OrderState.waiting_for_address)


@router.message(OrderState.waiting_for_address)
async def process_address(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    address = message.text

    from bot.database import add_order
    add_order(name, address)

    await message.answer(
        f"Спасибо, {name}!\n\n"
        f"Ваш заказ оформлен.\n"
        f"Адрес доставки: {address}"
    )

    await state.clear()
