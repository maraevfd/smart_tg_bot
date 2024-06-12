import os

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import google.generativeai as genai
from app.keyboards import main_keyboard

router = Router()

genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Gemini!\nНапиши мне что-нибудь')


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


@router.message()
async def send_echo(message: Message):
    response = model.generate_content(message.text)
    await message.reply(text=response.text)
