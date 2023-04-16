from telebot import types


class Phase:

    def __init__(check_function=None, *data):
        pass

    def on_return(self, menu, user=None, message=None):
        # Что должна делать функция на действия, совершенные после on_call
        # Что делать с нажатой кнопкой/введёнными даннывми и т.п.
        print('on_return')
        return user

    def on_call(self, menu, user, message):
        # ЧТо делает функция при вызове данной фазы
        print('on_call')
        pass

    def check_access(self, user, message):
        # Триггеры фазы
        print('check_access')
        pass

    def get_buttons(self, values, keys, step=0, cols=1, appender=False):
        buttons = []
        markup = types.InlineKeyboardMarkup()
        if appender is True:
            if len(values) % cols != 0:
                k = cols - (len(values) % cols)
                for i in range(k):
                    values.append(' ')
                    keys.append('Nan')

        for pos, data in enumerate(list(zip(values, keys))):
            text = data[0]
            callback = data[1]
            buttons.append(types.InlineKeyboardButton(
                text=text, callback_data=callback))
            if (pos + 1) % cols == 0:
                markup.add(*buttons)
                buttons = []

        while len(buttons) // cols > 0:
            markup.add(*buttons[:cols])
            buttons = buttons[cols:]

        markup.add(*buttons)
        return markup
