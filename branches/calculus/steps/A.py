from phase_pattern import *
from copy import deepcopy
from time import time
first = Phase()


def on_return(menu=None, user=None, message=None):
    setattr(user, 'lvl', 0)
    setattr(user, 'start_time', time())
    setattr(user , 'correct', 0)
    setattr(user , 'matches', 0)
    return user, 'NEXT'


def on_call(menu=None, user=None, message=None):
    MSG = 'Сравнения - это игра, в которой вам предстоит сравнивать два выражения и определять их соотношение (больше/меньше/равны)'
    markup = first.get_buttons(['Начать игру'], ['start_game'], cols=2)
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    if (message.type == 'callback') and (message.content in 'start_game'):
        return True
    else:
        return False


setattr(first, 'on_call', on_call)
setattr(first, 'check_access', check_access)
setattr(first, 'on_return', on_return)
