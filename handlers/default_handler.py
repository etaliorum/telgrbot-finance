from aiogram import types
from bot import dp


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer("Ok, Start")


@dp.message_handler(commands='help')
async def cmd_start(message: types.Message):
    await message.answer("Ok, Help!")
