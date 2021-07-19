from aiogram import types
from bot import dp
from database.query import insert_expenses
from filters.db_filters import parse_message


@dp.message_handler()
async def any_message(message: types.Message):
    #await parse_message(message.text, message.from_user.id)
    await message.answer(await parse_message(message.text, message.from_user.id))