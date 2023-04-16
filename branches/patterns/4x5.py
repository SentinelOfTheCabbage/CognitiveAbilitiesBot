from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def svg_to_png(filename='pattern.svg'):
    drawing = svg2rlg(filename)
    renderPM.drawToFile(drawing, '4x5.png', fmt='PNG')


def create_question_pattern():
    file_pattern = \
        u'''<svg version="1.1"
    baseProfile="full"
    width="400" height="500"
    xmlns="http://www.w3.org/2000/svg">

    <rect width="100%" height="100%" fill="#321414"/>
    <text x="200" y="50" font-size="22" text-anchor="middle" fill="white">How many COLOR_NAME squares?</text>

{}

    </svg>
    '''
    rect_pattern = '\t<rect x="{}" y = "{}" width="69" height="69" rx="15" fill="#123456"/>'
    rectangles = []
    for i in range(5):
        for j in range(4):
            rect = rect_pattern.format(
                50 + 77 * j, 100 + 11 + 77 * i)
            rectangles.append(rect)
    result = file_pattern.format('\n'.join(rectangles))
    with open('4x5.svg', 'w', encoding='cp1251') as file:
        file.write(result)

    svg_to_png(filename='4x5.svg')

create_question_pattern()
