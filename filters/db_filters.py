from datetime import datetime, timezone
from database.query import insert_expenses
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

available_categories = ['food', 'transport', 'other']


class InsertExpenses(StatesGroup):
    waiting_category_expense = State()
    waiting_amount_expense = State()


async def start_insert_expenses():
    await InsertExpenses.waiting_category_expense.set()


async def category_chosen(message, state):
    if message.text.lower() not in available_categories:
        await message.answer('Please use keyboard to chose category')
        return
    await state.update_data(chosen_category=message.text.lower())
    await InsertExpenses.next()
    await message.answer('Please enter you amount expense:')


async def amount_expense(message, state):
    user_data = await state.get_data()
    await message.answer(f"You added in {user_data['chosen_category']} category {message.text} UAH expense")
    await state.finish()


async def parse_message(string, user_id):
    list_categories = ['food', 'transport', 'other']
    lst = string.lower().split()
    dt = datetime.now(timezone.utc)

    for category in list_categories:
        if category in lst[0]:
            insert_expenses([user_id, category, lst[1], dt])
            return f'You have added {lst[1]} UAH of expenses to the {lst[0]}'
    return 'Invalid arguments. Please try example\n' \
           'food 300'


async def get_expenses(list_expenses):
    string = ''
    for item in list_expenses:
        string += f'In category {item[1]} you have been spent {item[0]} UAH\n'
    return string
