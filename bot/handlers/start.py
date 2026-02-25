from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.keyboards.main_menu import main_menu

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! Это твоя фундаментальная витрина 🚀\n\nВыбери действие:",
        reply_markup=main_menu
    )
