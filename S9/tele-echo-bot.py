from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def startCommand(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я могу поболтать')


def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')


# bad_list = инженер-конструктор Игорь, главный бухгалтер МАРИНА, токарь высшего разряда нИКОЛАй, директор аэлита
def change_list(update: Update, context: CallbackContext):
    msg = update.message.text
    # print(msg)
    items = msg.replace('/empl ', '').split(', ')
    update.message.reply_text(', '.join(el.title() for el in items))

# Нашаабв абв стабврока
def change_str(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.replace('/str ', '')
    update.message.reply_text(items.replace('абв', ''))



updater = Updater('5747203558:AAFta3KOWVkQtBSkJw5HDqMbuSoF0Y99E_E')


updater.dispatcher.add_handler(CommandHandler("start", startCommand))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('empl', change_list))
updater.dispatcher.add_handler(CommandHandler('str', change_str))

updater.start_polling()
updater.idle()

