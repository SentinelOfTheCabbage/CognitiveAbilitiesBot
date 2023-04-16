# pylint: disable=C0111
class User:

    def __init__(self, user_id, last_message, **kwargs):
        self.phase = 0
        self.lvl = 0
        self.id = user_id
        self.last_message = last_message
        self.mistakes = 0
        key = list(kwargs.keys())[0]
        if kwargs[key] is not None:
            for k in kwargs[key]:
                exec(f'self.{k} = \'{kwargs[key][k]}\'')

    def get_phase(self):
        return self.phase

    def __str__(self):
        data = {}
        data['phase'] = self.phase
        data['lvl'] = self.lvl

        keys = data.keys()
        result = ''
        for elem in keys:
            result += f'{elem}:\t {data[elem]}\n'

        return result

    def __dict__(self):
        data = {}
        data['phase'] = self.phase
        data['lvl'] = self.lvl
        return data

if __name__ == '__main__':
    u = User(123, 123)
    u.append_basket({'price': 500})
    print('Loaded')
