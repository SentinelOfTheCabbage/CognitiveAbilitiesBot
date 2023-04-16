from random import random, randrange, shuffle
import json

eng_chars = 'abcdefghijklmnopqrstuvwxyz'
rus_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def get_words():
    return words = [
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
    return [answer_index + 1, options]


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


def create_quest(lvl) -> tuple:
    word = get_params_by_lvl(lvl)
    ans = get_anagrams(word)
    return word, ans[0], ans[1]


if __name__ == '__main__':
    print(create_quest(0))
