from random import randint, randrange, shuffle


def get_num_division(number, count) -> str:
    if count == 1:
        return [number]
    if count == 2:
        return div2(number)
    if count == 3:
        return div3(number)


def div2(number) -> tuple:
    var = [-1, 1]
    shuffle(var)
    k = var[0]
    div = randint(3, 7)

    bound = (div - k) * number // (2 * div)
    delta = 0
    if bound > 0:
        delta = randrange(bound)

    alpha = (div - k) * number // div - k * delta
    beta = number - alpha
    return [alpha, beta]


def div3(number) -> tuple:
    alpha = beta = number // 3
    gamma = number - alpha - beta

    m = min(number // 7, number // 5)
    M = max(number // 7, number // 5) + 1
    var = [-1, 1]

    shuffle(var)
    k = var[0]

    delta = randrange(m, M)
    alpha += k * delta
    beta -= k * delta

    shuffle(var)
    k = var[0]
    delta = randrange(m, M)
    beta += k * delta
    gamma -= k * delta

    return [alpha, beta, gamma]


def get_param_by_lvl(lvl) -> tuple:
    if lvl < 3:
        return (1, 1)
    elif lvl < 6:
        return (2, 1)
    elif lvl < 9:
        return (2, 2)
    elif lvl < 12:
        return (3, 2)
    else:
        return (3, 3)


def format_options(options):
    answer = []
    for elem in options:
        answer.append([])
        for pos, num in enumerate(elem):
            if pos == 0 or num < 0:
                answer[-1].append(str(num))
            elif num > 0:
                answer[-1].append(f'+{num}')

    return (''.join(answer[0]), ''.join(answer[1]))


def create_quest(lvl):
    params = get_param_by_lvl(lvl)
    question_type = randrange(3) - 1
    a, b = get_numbers(question_type, lvl)

    a = get_num_division(a, params[0])
    b = get_num_division(b, params[1])
    options = [a, b]
    shuffle(options)
    if question_type == -1:
        if sum(options[0]) < sum(options[1]):
            answer = -1
        else:
            answer = 1
    elif question_type == 1:
        if sum(options[0]) > sum(options[1]):
            answer = -1
        else:
            answer = 1
    elif question_type == 0:
        question_type = [-1, 1][randrange(2)]
        answer = 0
    # print(options)
    for pos, elem in enumerate(options):
        if elem[0] < 0:
            if len(options[pos]) > 1:
                options[pos][0] = -elem[0]
                options[pos][1] -= 2 * elem[0]

    options = format_options(options)
    return (question_type, answer, options)


def get_numbers(question_type, lvl):
    ans = []
    if question_type == 0:
        num = randint(-500, 500)
        ans = (num, num)
    elif question_type == -1:
        num1 = randint(-500, 500)
        num2 = num1 + randint(1, 50)
        ans = (num1, num2)
    elif question_type == 1:
        num1 = randint(-500, 500)
        num2 = num1 - randint(1, 50)
        ans = (num1, num2)
    if lvl < 6:
        return list(map(abs, ans))
    else:
        return ans

if __name__ == '__main__':
    ans = create_quest(100)
    print(ans)
    # if ans[1] == 0 and sum(ans[2][0]) != sum(ans[2][1]):
    #     print('\t', ans)
    # else:
    #     print()
