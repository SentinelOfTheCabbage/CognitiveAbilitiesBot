from random import randint, randrange, shuffle


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
    return(ans, seq, list(map(str, options)))
