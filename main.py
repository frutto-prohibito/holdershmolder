import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.handlers.start import router as start_router

from bot.handlers.order import router as order_router

app = FastAPI()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(order_router)

@app.get("/")
async def root():
    return {"status": "Bot is running"}

async def start_bot():
    await dp.start_polling(bot)

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(start_bot())
