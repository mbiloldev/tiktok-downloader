import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor
from api import download_instagram_video

API_TOKEN = 'bot_token_hero'

# Bot va dispatcher obyektlarini yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# /start komandasi uchun handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Instagram videolarini yuklash uchun URL yuboring.")


# URL uchun handler
@dp.message_handler()
async def fetch_video(message: types.Message):
    url = message.text
    await message.reply("Videoni yuklamoqdamiz, biroz kuting...")

    video_file = download_instagram_video(url)
    if video_file:
        await message.reply_video(video=InputFile(video_file))
        os.remove(video_file)  # Faylni o'chirib tashlash
    else:
        await message.reply("Video yuklashda xato yuz berdi.")


# Xatolarni qayd qilish
@dp.errors_handler()
async def error_handler(update, error):
    print(f"Update: {update} caused error: {error}")
    return True


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
