from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Gemini')],
    [KeyboardButton(text='Kantor')],
    [
        KeyboardButton(text='BlaBlaCar'),
        KeyboardButton(text='Puk'),
    ]
])
