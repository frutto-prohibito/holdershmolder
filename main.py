import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://holdershmolder.onrender.com{WEBHOOK_PATH}"

app = FastAPI()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ---------- Telegram handlers ----------

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Это твоя фундаментальная витрина 🚀")

# ---------- Webhook endpoint ----------

@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}

# ---------- Startup event ----------

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook установлен:", WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
