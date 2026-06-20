import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = '7044287189:AAF9uXbbz6A3Pq_cG1iHQ6FB6J9DoxkrHVc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Turli javoblar ro'yxati
RESPONSES = [
    "Salom!",
    "Alik!",
    "Qanday yordam bera olaman?",
    "Siz bilan suhbatlashish juda yoqimli!",
    "Salom, do'stim!",
    "Hush kelibsiz!",
    "Qalaysiz?",
    "Sizni ko'rishdan xursandman!",
    "Nima yangiliklar?",
    "Boshqa qanday savollaringiz bor?",
    "Bugun kayfiyatingiz qanday?",
    "Bilasizmi, men yangi narsalarni o'rganmoqdaman!",
    "Hayotda qanday o'zgarishlar bo'ldi?",
    "Hush bo'ling!",
    "Yordamingiz kerak bo'lsa, shu yerdaman!",
    "Bugun qanday kechdi?",
    "Sizni yana ko'rishdan xursandman!",
    "Nimadir haqida suhbatlashishni xohlaysizmi?",
    "Bu yerda nima yangiliklar bor?",
    "Siz bilan gaplashish juda yoqimli!"
]


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Menga har qanday xabar yozing va men javob beraman.")


@dp.message_handler()
async def respond_to_message(message: types.Message):
    user_text = message.text
    # Tasodifiy javobni tanlash
    response = random.choice(RESPONSES)
    await message.reply(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
