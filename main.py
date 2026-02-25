import asyncio
import logging

from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from bot.config import BOT_TOKEN
from bot.handlers.start import router as start_router
from bot.handlers.order import router as order_router

app = FastAPI()

# --- Telegram bot setup ---
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(order_router)


@app.get("/")
async def root():
    return {"status": "service is running"}


async def run_bot_polling():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


@app.on_event("startup")
async def on_startup():
    # запускаем бота параллельно веб-серверу
    asyncio.create_task(run_bot_polling())
