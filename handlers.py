from aiogram import types


# функция, обрабатывающая команду /start
async def start(message: types.Message):
    await message.answer("Привет!\nЗачем пришёл?")


# функция, которая отвечает на сообщение
# текстом
async def echo(message: types.Message):
    await message.answer("Сам ты: " + message.text)
