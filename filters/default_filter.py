def command_start():
    string = 'Hello!, this is Bot for Accounting Finance\n' \
             'show command /help'
    return string


def command_help():
    string = '/categories - Show Categories\n' \
             '/expenses_month - Show expenses month\n' \
             '/expenses_week -- Expenses on week\n' \
             '/expenses_day -- Expenses today'
    return string


def command_categories():
    string = '/food\n' \
             '/tranport\n' \
             '/other'
    return string
