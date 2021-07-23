from aiogram import types
from bot import dp
from filters.db_filters import parse_message, get_expenses
from database.query import get_query_expenses
from aiogram.dispatcher import FSMContext
from filters.db_filters import start_insert_expenses, category_chosen, amount_expense, InsertExpenses

available_categories = ['food', 'transport', 'other']


@dp.message_handler(state=InsertExpenses.waiting_category_expense)
async def start_chosen_category(message: types.Message, state: FSMContext):
    await category_chosen(message, state)


@dp.message_handler(state=InsertExpenses.waiting_amount_expense)
async def start_chosen_amount(message: types.Message, state: FSMContext):
    await amount_expense(message, state)
    await message.answer('What do you want to do?', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands='insert_expense')
async def cmd_start_insert_expenses(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in available_categories:
        keyboard.add(category)
    await message.answer('Enter category expense', reply_markup=keyboard)
    await start_insert_expenses()


@dp.message_handler(commands='get_expenses')
async def cmd_get_expenses(message: types.Message):
    await message.answer(await get_expenses(get_query_expenses(message.from_user.id)))


# @dp.message_handler()
# async def any_message(message: types.Message):
#     await message.answer(await parse_message(message.text, message.from_user.id))
