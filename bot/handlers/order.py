from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states import OrderState

router = Router()


# 1️⃣ Нажали кнопку "Оформить заказ"
@router.message(lambda message: message.text == "🛍 Оформить заказ")
async def start_order(message: Message, state: FSMContext):
    await state.set_state(OrderState.waiting_for_name)
    await message.answer("Введите ваше имя:")


# 2️⃣ Ввели имя
@router.message(OrderState.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(OrderState.waiting_for_address)
    await message.answer("Введите адрес доставки:")


# 3️⃣ Ввели адрес
@router.message(OrderState.waiting_for_address)
async def process_address(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    address = message.text

from bot.database import add_order

# сохраняем заказ в базу
add_order(name, address)
    
    await message.answer(
        f"Спасибо, {name}!\n\n"
        f"Ваш заказ оформлен.\n"
        f"Адрес доставки: {address}"
    )

    await state.clear()
