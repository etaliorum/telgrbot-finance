from aiogram import types
from bot import dp
from filters.db_filters import parse_message
from database.query import get_expenses


@dp.message_handler()
async def any_message(message: types.Message):
    await message.answer(await parse_message(message.text, message.from_user.id))


@dp.message_handler(commands='get_expenses')
async def cmd_get_expenses(message: types.Message):
    await message.answer(get_expenses(message.from_user.id))
