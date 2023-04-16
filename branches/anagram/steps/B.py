from phase_pattern import *
from copy import deepcopy
from random import random, randrange, shuffle
from time import time
second = Phase()


def on_return(menu=None, user=None, message=None):
    if message.content == user.answer:
        user.lvl += 1
        user.correct += 1
        menu.bot.answer_callback_query(
            message.callback.id, text='Верный ответ', show_alert=False)
    else:
        user.lvl -= 1
        menu.bot.answer_callback_query(
            message.callback.id, text='Неверный ответ', show_alert=False)
    user.matches += 1
    if (time() - user.start_time) >= 60:
        return user, 'NEXT'

    return user, 'CURRENT'


def on_call(menu=None, user=None, message=None):
    eng_chars = 'abcdefghijklmnopqrstuvwxyz'
    rus_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def get_words():
        return [
            # 4
            'word',    'hawk',    'flip',    'bear',
            'dice',    'clam',    'keep',    'lent',
            'rich',    'shot',    'zone',    'long',
            'rise',    'join',    'road',    'dirt',
            'fear',

            # 5
            'world',    'jewel',    'claim',    'dodge',
            'depth',    'bunny',    'label',    'curse',
            'jeans',    'basic',    'cover',    'equip',
            'force',    'glide',    'imply',    'lader',
            'month',    'ocean',    'quick',

            # 6
            'flower',    'junior',    'police',    'couple',
            'poison',    'finger',    'leader',    'bullet',
            'friend',    'anyone',    'basket',    'garlic',
            'jaguar',    'nugget',    'pepper',    'softer',
            'thrill',    'vacant',    'warmth',

            # 7
            'thunder',    'reverse',    'boolean',    'harvest',
            'ability',    'cartoon',    'digital',    'freeman',
            'kinetic',    'mistake',    'optical',    'polygon',
            'healthy',    'krypton',
        ]

    words = get_words()
    if getattr(user, 'words', None) == None:
        setattr(user, 'words', words)

    def get_anagrams(word: str) -> list:
        tmp = list(word)
        shuffle(tmp)
        answer = ''.join(tmp)
        options = [answer]

        for _ in range(3):
            new_word = list(word)
            replaces_count = randrange(3) + 1
            for _ in range(replaces_count):
                pos = randrange(len(new_word))
                tmp = new_word[pos]
                if tmp in eng_chars:
                    while tmp == new_word[pos]:
                        ind = randrange(len(new_word))
                        tmp = eng_chars[ind]
                elif tmp in rus_chars:
                    while tmp == word[pos]:
                        ind = randrange(len(new_word))
                        tmp = rus_chars[ind]

            new_word[pos] = tmp
            shuffle(new_word)
            options.append(''.join(new_word))

        shuffle(options)
        answer_index = options.index(answer)
        return [answer_index, options]

    def get_params_by_lvl(lvl: int) -> int:
        if lvl < 2:
            var = [w for w in words if len(w) == 4]
            return var[randrange(len(var))]
        elif lvl < 5:
            var = [w for w in words if len(w) == 5]
            return var[randrange(len(var))]
        elif lvl < 8:
            var = [w for w in words if len(w) == 6]
            return var[randrange(len(var))]
        else:
            var = [w for w in words if len(w) == 7]
            return var[randrange(len(var))]

    def create_quest(word, lvl) -> tuple:
        ans = get_anagrams(word)
        return word, ans[0], ans[1]

    ind = randrange(len(words))
    word = user.words[ind]
    user.words.pop(ind)

    word, answer, options = create_quest(word, user.lvl)
    setattr(user, 'answer', options[answer])
    values = []
    callbacks = []
    for var in options:
        values.append(var)
        callbacks.append(var)

    markup = second.get_buttons(values, callbacks)
    MSG = f'Найдите анаграмму для слова: {word}'
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    if message.type == 'callback':
        return True
    else:
        return False

setattr(second, 'on_call', on_call)
setattr(second, 'check_access', check_access)
setattr(second, 'on_return', on_return)
