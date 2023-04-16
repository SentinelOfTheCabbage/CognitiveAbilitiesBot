from phase_pattern import *
from copy import deepcopy
from time import time
first = Phase()


def on_return(menu=None, user=None, message=None):
    setattr(user, 'lvl', 0)
    setattr(user, 'start_time', time())
    setattr(user, 'matches', 0)
    setattr(user, 'correct', 0)
    return user, 'NEXT'


def on_call(menu=None, user=None, message=None):
    MSG = 'Анаграммы - в этом задании вам необходимо как можно большее число раз найти анаграмму загаданного слова. Анаграммой называется сочетание букв образованное путём перестановки букв, составляющих начальное слово. Например "ргамнаама" является анаграммой слова "анаграмма", но "рганама" - нет.'
    values = ['Начать игру']
    callbacks = ['start_game']
    user.mistakes = 0
    markup = first.get_buttons(values, callbacks)
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    if (message.type == 'callback') and (message.content == 'start_game'):
        return True
    else:
        return False


setattr(first, 'on_call', on_call)
setattr(first, 'check_access', check_access)
setattr(first, 'on_return', on_return)
