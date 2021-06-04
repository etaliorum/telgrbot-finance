from aiogram import types
from bot import dp
from filters.default_filter import command_start, command_help, command_categories


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(command_start())


@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await message.answer(command_help())


@dp.message_handler(commands='categories')
async def cmd_categories(message: types.Message):
    await message.answer(command_categories())
