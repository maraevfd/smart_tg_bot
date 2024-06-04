import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

bot = Bot(token=os.environ.get('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Gemini!\nНапиши мне что-нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


@dp.message()
async def send_echo(message: Message):
    response = model.generate_content(message.text)
    await message.reply(text=response.text)


if __name__ == '__main__':
    dp.run_polling(bot)
