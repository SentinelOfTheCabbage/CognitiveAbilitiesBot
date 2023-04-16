from phase_pattern import *
from copy import deepcopy
from time import time

first = Phase()


def on_return(menu=None, user=None, message=None):
    setattr(user, 'lvl', 0)
    setattr(user, 'correct', 0)
    setattr(user, 'matches', 0)
    setattr(user, 'start_time', time())
    return user, 'NEXT'


def on_call(menu=None, user=None, message=None):
    MSG = 'Подсчёты - игра, в которой вам престоит оперативно считать количество элементов соответствующего цвета. Общее число элементов варьируется в зависимости от ваших успехов'
    markup = first.get_buttons(['Начать игру'], ['start_game'])
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    if (message.type == 'callback') and (message.content == 'start_game'):
        return True
    else:
        return False


setattr(first, 'on_call', on_call)
setattr(first, 'check_access', check_access)
setattr(first, 'on_return', on_return)
