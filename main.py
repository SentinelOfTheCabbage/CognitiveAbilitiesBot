#pylint: disable=C0111, W0401,W0614
from telebot        import TeleBot, types
from main_menu      import *
from branches       import *
from Messages       import *
from NewSettings    import *
from time           import sleep

BOT = TeleBot(TOKEN)
MAIN_MENU = main_menu(BOT)


@BOT.message_handler(func=lambda message: True)
def reaction(message) -> None:
    MAIN_MENU.get_reaction(message=message)

@BOT.callback_query_handler(func=lambda call: call.data != 'Nan')
def clbk(call) -> None:
    MAIN_MENU.get_reaction(callback=call)

while True:
    try:
        print('STARTING')
        BOT.polling(none_stop=True)
    except:
        # BOT.stop_polling()
        # sleep(5)
        break