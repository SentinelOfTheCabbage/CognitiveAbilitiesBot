from phase_pattern import *
from copy import deepcopy
from time import time
from random import shuffle
from time import time

third = Phase()


def on_return(menu=None, user=None, message=None):
    emojies = {'check': '\u2714', 'cross': '\u274C'}
    values = user.options
    index = values.index(message.content)
    if message.content in user.removed_part:
        user.removed_part.remove(message.content)
        values[index] = emojies['check']
    elif message.content not in emojies.values():
        values[index] = emojies['cross']
        user.cur_lvl_mistakes += 1
        user.mistakes += 1

    MSG = f'Какие числа были удалены из последовательности?\n{"  ".join(user.ask_seq)}'
    callbacks = values
    markup = third.get_buttons(values, callbacks, cols=3)
    menu.bot.edit_message_text(
        chat_id=user.id, message_id=user.prev_msg, text=MSG, reply_markup=markup)

    if (user.mistakes >= 3) or (time() - user.start_time >= 60):
        return user, 'NEXT'
    elif user.cur_lvl_mistakes == 2:
        user.matches += 1
        menu.bot.answer_callback_query(
            message.callback.id, text='Неверный ответ', show_alert=False)
        if user.lvl > 0:
            user.lvl -= 1
        return user, 'PREVIOUS'
    elif len(user.removed_part) == 0:
        user.matches += 1
        user.correct += 1
        user.lvl += 1
        return user, 'PREVIOUS'
    else:
        return user, 'CURRENT'


def on_call(menu=None, user=None, message=None):
    pass


def check_access(menu, user, message):
    if message.type == 'callback' and message.content in user.options:
        return True


setattr(third, 'on_call', on_call)
setattr(third, 'check_access', check_access)
setattr(third, 'on_return', on_return)
