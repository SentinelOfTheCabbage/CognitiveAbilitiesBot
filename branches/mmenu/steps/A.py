from phase_pattern import *
from copy import deepcopy
first = Phase()


def on_return(menu=None, user=None, message=None):
    return user, None


def on_call(menu=None, user=None, message=None):
    MSG = 'Вас приветствует чат-бот для тренировки когнитивных способностей. Вашему выбору представляется одна из следующих игр:'
    values = ['Сыщик','Анаграммы','Сравнения','Последовательности','Подсчёты','Синонимы']
    replies = ['secret_room','anagrams','calculus','sequences','squares','synonyms']
    markup = first.get_buttons(values,replies, cols=1)
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    return False



setattr(first, 'on_call', on_call)
setattr(first, 'check_access', check_access)
setattr(first, 'on_return', on_return)