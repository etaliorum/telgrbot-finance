from aiogram import types
from bot import dp
from filters.default_filter import command_start, command_help


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(command_start())


@dp.message_handler(commands='help')
async def cmd_start(message: types.Message):
    await message.answer(command_help())
