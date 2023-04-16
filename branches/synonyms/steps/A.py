from phase_pattern import *
from copy import deepcopy
from time import time
first = Phase()


def on_return(menu=None, user=None, message=None):
    words = [
        ['jokey', 'comic', 'risible', 'sensible', 'serious', 'grave'],
        ['accepted', 'approved', 'admitted', 'refused', 'rejected', 'denied'],
        ['reliable', 'faithful', 'honest', 'remorseful', 'mournful', 'sorry'],
        ['prickly', 'troublesome', 'vexatious',
            'amicable', 'peaceful', 'friendly'],
        ['strengthened', 'intensified', 'hardened',
            'weakened', 'hindered', 'impaired'],
        ['worthless', 'pointless', 'vile', 'extraordinary', 'superb', 'quality'],
        ['irked', 'piqued', 'irritated', 'settled', 'peaceful', 'relaxed'],
        ['peaceable', 'harmonious', 'civilized',
            'militant', 'hostile', 'belligerent'],
        ['lively', 'exciting', 'active', 'gray', 'tedious', 'sluggish'],
        ['liberated', 'released', 'emancipated', 'tactless', 'nasty', 'uncaring'],
        ['gleeful', 'joyous', 'jolly', 'melancholic', 'depressed', 'sorry'],
        ['handsome', 'elegant', 'cute', 'filthy', 'infected', 'impure'],
        ['authentic', 'genuine', 'real', 'fabricated', 'fake', 'pretended'],
        ['rough', 'unfinished', 'rugged', 'entertaining', 'darling', 'delightful'],
        ['confirmed', 'acknowledged', 'authenticated',
            'disused', 'desolate', 'deserted'],
        ['explosive', 'volcanic', 'sudden', 'unremitting', 'resolute', 'faithful'],
        ['barbed', 'malicious', 'venomous', 'quiet', 'soothing', 'mellow'],
        ['reasonable', 'equitable', 'judicious', 'grouchy', 'cranky', 'prickly'],
        ['amusing', 'entertaining', 'delightful', 'boring', 'tedious', 'tiring'],
        ['snide', 'insulting', 'mocking', 'shiny', 'luminous', 'glowing'],
        ['fortunate', 'lucky', 'favorable', 'failing', 'ineffectual', 'abortive'],
        ['defeated', 'beaten', 'overpowered', 'honest', 'virtuous', 'pure'],
        ['appreciated', 'admired', 'regarded',
            'undesirable', 'unwanted', 'detestable'],
        ['deserted', 'forsaken', 'quit', 'attendant', 'affiliated', 'related'],
        ['clear', 'sure', 'obvious', 'infected', 'impure', 'filthy'],
        ['banished', 'abolished', 'deported', 'allowed', 'granted', 'admitted'],
        ['disrespectful', 'impertinent', 'rude',
            'courteous', 'obedient', 'admiring'],
        ['serene', 'restful', 'placid', 'gushing', 'flattering', 'fawning'],
        ['precise', 'mathematical', 'exact', 'withdrawn', 'distant', 'quiet'],
        ['even', 'fair', 'equal', 'bizarre', 'senseless', 'unreasonable'],
        ['kittenish', 'flirtatious', 'lively',
            'perilous', 'menacing', 'hazardous'],
        ['foiled', 'defeated', 'beaten', 'placid', 'quiet', 'pacific'],
        ['devilish', 'thorny', 'problematic', 'serious', 'sensible', 'grave'],
        ['pristine', 'clean', 'virgin', 'unreadable', 'stony', 'blank'],
        ['chastised', 'rebuked', 'scolded', 'informed', 'briefed', 'educated'],
        ['delicious', 'good-tasting', 'succulent',
            'ridiculous', 'stupid', 'foolish'],
        ['frank', 'open', 'obvious', 'slippery', 'evasive', 'shifty'],
        ['glorious', 'marvelous', 'majestic', 'embarrassed', 'ashamed', 'humbled'],
        ['mischievous', 'troublesome', 'misbehaving',
            'leading', 'ruling', 'commanding'],
        ['capable', 'qualified', 'accomplished', 'innocent', 'pure', 'virtuous']
    ]

    setattr(user, 'words', words)
    setattr(user, 'start_time', time())
    setattr(user, 'lvl_count', -1)
    setattr(user, 'correct', 0)
    setattr(user, 'matches', 0)
    return user, 'NEXT'


def on_call(menu=None, user=None, message=None):
    markup = first.get_buttons(
        ['Начать игры'], ['start_game'], cols=2)

    MSG = 'Синонимы - это игра, в которой вам предстоит находить из ряда предлагаемых слов ровно два синонима к изначальному слову'
    menu.bot.send_message(user.id, MSG, reply_markup=markup)


def check_access(menu, user, message):
    if (message.type == 'callback') and (message.content == 'start_game'):
        return True
    else:
        return False


setattr(first, 'on_call', on_call)
setattr(first, 'check_access', check_access)
setattr(first, 'on_return', on_return)
