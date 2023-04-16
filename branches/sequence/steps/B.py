from phase_pattern import *
from copy import deepcopy
from time import time
from random import randint, randrange, shuffle

second = Phase()


def on_return(menu=None, user=None, message=None):
    if time() - user.start_time >= 60:
        return user, 'NEXT'
    if int(message.content) == user.answer:
        user.correct += 1
        user.lvl += 1
    elif message.type == 'callback':
        menu.bot.answer_callback_query(
            message.callback.id, text='Неверный ответ', show_alert=False)
    user.matches += 1
    return user, 'CURRENT'


def on_call(menu=None, user=None, message=None):
    def get_params_by_lvl(lvl):
        if lvl < 3:
            return (1, 2, False)
        elif lvl < 7:
            return (1, 2, True)
        elif lvl < 10:
            return (2, 3, 4, False)
        else:
            return (2, 3, 4, True)

    def generate_fib(c=0):
        first = randrange(10) + 1
        second = randrange(10) + 1
        seq = []
        for i in range(5):
            seq.append(first)
            first, second = second, first + second

        return seq[-1], seq[:-1]

    def generate_arifm(c=0):
        a = randrange(10) + 1
        b = randrange(10) + 1

        seq = [(a + i) * b + c for i in range(5)]
        return seq[-1], seq[:-1]

    def generate_polynom(c=0):
        a = randrange(10) + 1
        b = randrange(5)

        seq = [(a + i)**b + c for i in range(5)]
        return seq[-1], seq[:-1]

    def generate_pokazat(c=0):
        a = randrange(10) + 1
        b = randrange(5)
        seq = [a**(b + 1) + c for i in range(5)]
        return seq[-1], seq[:-1]

    def get_quest_funcs(index):
        return [
            generate_fib,
            generate_arifm,
            generate_polynom,
            generate_pokazat,
        ][index]

    def create_quest(lvl):
        params = get_params_by_lvl(lvl)
        quests = params[:-1]
        quest_num = quests[randrange(len(quests))]
        quest_func = get_quest_funcs(quest_num)
        if params[-1]:
            ans, seq = quest_func(c=randrange(10) + 1)
        else:
            ans, seq = quest_func()

        index = randrange(4)
        deltas = [pos - index for pos in range(4)]
        options = [ans + d for d in deltas]
        return(ans, list(map(str, seq)), list(map(str, options)))

    answer, seq, options = create_quest(user.lvl)
    setattr(user, 'options', options)
    setattr(user, 'answer', answer)
    MSG = 'Какого числа не хватает в последовательности?\n'
    MSG += '\t'.join(seq)
    markup = second.get_buttons(options, options, cols=2)
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    if (message.type == 'callback') and (message.content in user.options):
        return True
    else:
        return False

setattr(second, 'on_call', on_call)
setattr(second, 'check_access', check_access)
setattr(second, 'on_return', on_return)