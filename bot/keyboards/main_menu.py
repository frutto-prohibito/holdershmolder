
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Портфель")],
        [KeyboardButton(text="📈 Аналитика")],
        [KeyboardButton(text="ℹ️ О проекте")]
    ],
    resize_keyboard=True
)
