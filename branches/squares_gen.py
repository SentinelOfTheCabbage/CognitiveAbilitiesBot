
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from random import randint, randrange, shuffle


def svg_to_png(filename='pattern.svg'):
    drawing = svg2rlg(filename)
    renderPM.drawToFile(drawing, 'quest.png', fmt='PNG')


def get_color_base(count):
    colors = {
        'orange':   '#e05a00',
        'yellow':   '#ffcc00',
        'green':   '#00b300',
        'blue':   '#005aeb',
        'red':   '#ff2400',
    }
    keys = list(colors.keys())
    shuffle(keys)
    answer = {'white': '#FFFFFF'}
    answer = dict(**answer, **{key: colors[key] for key in keys[:count]})
    return answer


def get_params_by_lvl(lvl: int) -> str:
    answer = [
        ('3x4', 1),
        ('4x4', 2),
        ('4x5', 2),
        ('4x6', 2),
        ('5x6', 2),
    ]
    if lvl < 2:
        return answer[0]
    elif lvl < 4:
        return answer[1]
    elif lvl < 7:
        return answer[2]
    elif lvl < 10:
        return answer[3]
    else:
        return answer[-1]


def get_quest(lvl):
    filename, color_count = get_params_by_lvl(lvl)
    with open(f'patterns/{filename}.svg', 'r', encoding='utf-8') as file:
        pattern = file.read()

    size = int(filename[0]) * int(filename[2])
    color_base = get_color_base(color_count)

    color_count += 1
    color_names = list(color_base.keys())
    answer_color = color_names[randrange(color_count)]
    answer_count = 0
    filler = []
    for _ in range(size):
        key = color_names[randrange(color_count)]
        filler.append(color_base[key])
        if key == answer_color:
            answer_count += 1

    res = pattern.replace('#123456', '{}')
    res = res.format(*filler)
    res = res.replace('321414', '000000')
    res = res.replace('COLOR_NAME', answer_color)
    with open('question.svg', 'w', encoding='utf-8') as file:
        file.write(res)
    svg_to_png(filename='question.svg')

    pos = randrange(4)

    return answer_count, list(map(str, [ind + answer_count - pos for ind in range(4)]))

if __name__ == '__main__':
    print(get_quest(2))
