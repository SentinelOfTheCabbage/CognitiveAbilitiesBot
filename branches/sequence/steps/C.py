from phase_pattern import *
from copy import deepcopy
from time import time

third = Phase()


def on_return(menu=None, user=None, message=None):
    return user, None


def on_call(menu=None, user=None, message=None):
    X = user.correct
    Y = user.matches
    MSG = f'Ваше время истекло\nЧисло верных ответов: {X} из {Y} (~ {round(X/Y,2)*100}%)'
    markup = third.get_buttons(['Вернуться в меню'], ['/start'])
    menu.bot.send_message(user.id, MSG, reply_markup=markup)
    del menu.current_users[user.id]


def check_access(menu, user, message):
    return False


def on_undo(menu=None, user=None, message=None):
    user.basket = user.basket[:-1]
    return user


setattr(third, 'on_call', on_call)
setattr(third, 'check_access', check_access)
setattr(third, 'on_return', on_return)
setattr(third, 'on_undo', on_undo)
# del on_call, on_return, check_access
