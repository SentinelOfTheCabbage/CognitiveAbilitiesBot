from random import randrange, random, shuffle, randint


def get_params_by_lvl(lvl: int) -> tuple:
    result = [
        (3, 1), (4, 1), (3, 2), (4, 2),
        (5, 1), (5, 2), (5, 3), (6, 1),
        (6, 2), (6, 3), (7, 1), (7, 2),
        (7, 3), (8, 1), (8, 2), (8, 3),
    ]
    if lvl > 15:
        return result[15]

    return result[lvl]


def same_numbers() -> list:
    return {
        '0': '8',
        '1': '7',
        '2': '5',
        '3': '8',
        '4': '1',
        '5': '2',
        '6': '9',
        '7': '1',
        '8': '3',
        '9': '6',
    }


def get_sames(num: int) -> tuple:
    tmp = list(str(num))
    sames = same_numbers()
    for pos, char in enumerate(tmp):
        tmp[pos] = sames[char]
    same_num = int(''.join(tmp))
    return (num, same_num, int((num + same_num) / 2))


def generate_answers(real_answers) -> tuple:
    options = set()
    for elem in real_answers:
        options |= set(get_sames(elem))
    while len(options) < 3 * len(real_answers) - (len(real_answers) - len(set(real_answers))):
        options.add(randint(1, 99))

    options -= set(real_answers)
    options = list(options) + real_answers
    shuffle(options)
    return options


def remove_some_nums(sequence: list, deletions: int) -> tuple:
    removed = []
    result_seq = sequence
    for _ in range(deletions):
        pos = randrange(len(result_seq))
        removed.append(result_seq.pop(pos))
    return result_seq, removed


def start_sequence(count) -> list:
    answer = []
    for _ in range(count):
        answer.append(randint(1, 99))
    return answer


def create_quest(lvl):
    count, deletions = get_params_by_lvl(lvl)
    seq = start_sequence(count)
    seq, rem = remove_some_nums(seq, deletions)
    options = generate_answers(rem)

    def int_to_str(seq: list) -> list:
        return list(map(str, seq))

    return (int_to_str(seq + rem), int_to_str(seq), int_to_str(rem), int_to_str(options))


if __name__ == '__main__':
    print(create_quest(50))
