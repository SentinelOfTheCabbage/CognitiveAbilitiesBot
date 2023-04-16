from phase_pattern import *
from copy import deepcopy
from time import time
from random import randrange, shuffle
second = Phase()


def on_return(menu=None, user=None, message=None):
    if time() - user.start_time > 60:
        return user, 'NEXT'
    else:
        return user, 'CURRENT'


def on_call(menu=None, user=None, message=None):
    def create_quest(word):
        ans = word[1:3]
        q = word[1:]
        shuffle(q)
        return (word[0], [q.index(word) for word in ans], q)

    ind = randrange(len(user.words))
    question, ans_ind, options = create_quest(user.words[ind])
    user.words.pop(ind)
    MSG = f'Find two synonyms for word "{question}"'
    setattr(user, 'answer', [options[index] for index in ans_ind])
    setattr(user, 'options', options)
    setattr(user, 'question', question)

    user.lvl_count += 1
    markup = second.get_buttons(options, options, cols=1)
    message = menu.bot.send_message(user.id, MSG, reply_markup=markup)
    setattr(user, 'prev_msg', message.message_id)


def check_access(menu, user, message):
    MSG = f'Find synonyms for word "{user.question}"'
    if time() - user.start_time > 60:
        return True

    if message.type == 'callback' and message.content in user.answer:
        index = user.options.index(message.content)
        user.options[index] = '\u2705'
        user.answer.remove(message.content)
        markup = second.get_buttons(user.options, user.options, cols=1)
        menu.bot.edit_message_text(
            chat_id=user.id, message_id=user.prev_msg, text=MSG, reply_markup=markup)

    elif message.type == 'callback' and message.content in user.options:
        index = user.options.index(message.content)
        user.options[index] = '\u274C'
        markup = second.get_buttons(user.options, user.options, cols=1)
        menu.bot.edit_message_text(
            chat_id=user.id, message_id=user.prev_msg, text=MSG, reply_markup=markup)

    if len(user.answer) == 0:
        user.correct += 1
        user.matches += 1
        return True
    else:
        user.matches += 1
        return False


setattr(second, 'on_call', on_call)
setattr(second, 'check_access', check_access)
setattr(second, 'on_return', on_return)
