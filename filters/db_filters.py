from datetime import datetime, timezone

from database.query import insert_expenses


async def parse_message(string, user_id):
    list_categories = ['food', 'transport', 'other']
    lst = string.lower().split()
    dt = datetime.now(timezone.utc)

    for category in list_categories:
        if category in lst[0]:
            insert_expenses([user_id, category, lst[1], dt])
            return 'Added'
    return 'Invalid arguments'


async def all_expenses(list_expenses):
    string = ''
    list_categories = ['food', 'transport', 'other']
    for item in list_expenses:
        string += f'In category {item[1]} you have been spent {item[0]} UAH\n'
    return string
