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
    MSG = 'Вам даётся последовательность чисел, после того, как вы её запомните, вашей задачей будет восстановление удалённых элементов последовательности. Т.е если изначально дана последовательность 1 2 3 4, а после запоминания лишь 2 3 _ _, то из списка предлагаемых чисел вам нужно будет выбрать лишь 1 и 4'
    markup = first.get_buttons(['Начать'], ['start'])
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    if (message.type == 'callback') and (message.content == 'start'):
        return True
    else:
        return False


setattr(first, 'on_call', on_call)
setattr(first, 'check_access', check_access)
setattr(first, 'on_return', on_return)
