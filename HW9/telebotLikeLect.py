import telegram
from telegram import Update  #pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
import datetime
# from spy import *
from mySupersecretToken import Get_my_Tg_taken, Get_my_Weather_taken
from WeatherForecast import Get_weather
from сurrency import Get_currency

def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close() 

def hello_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Hi {update.effective_user.first_name}! I'm a prisoner of this bot."\
    "\n Hope you will help me to find freedom.")

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Hi {update.effective_user.first_name}!"\
    "\n I can tell you about myself."\
    "\nJust type /hello to know me better. \n"\
    "\n As well you can use following comands:"\
    "\n  /c <3 digit value code> to see currency of value e.g. USD or EUR>"
    "\n /w <city> Hope to see weather forecast for entered city")

def weather_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    city = items[1]
    update.message.reply_text(f'{Get_weather(city, Get_my_Weather_taken())}')

def currency_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    currencyCode = context.args[0].upper()
    #msg.upper().split() # /sum 123 534543
    update.message.reply_text(f'{Get_currency(currencyCode)}')

def Calculator(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)

    x = int(context.args[0])
    action = context.args[1]
    y = int(context.args[2])

    if action == "+":
        update.message.reply_text(f'{x} {action} {y} = {x + y}')
    elif action == "-":
        update.message.reply_text(f'{x} {action} {y} = {x - y}')
    elif action == "*":
        update.message.reply_text(f'{x} {action} {y} = {x * y}')
    elif action == "/":
        update.message.reply_text(f'{x} {action} {y} = {x / y}')

    #msg.upper().split() # /sum 123 534543

updater = Updater(Get_my_Tg_taken())

# обработка команды старт (создаем Inline клавиатуру)
def startCommand(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Поздороваться', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Help', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('weather', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('currency', callback_data='buttonD')
    buttonE = telegram.InlineKeyboardButton('calculator', callback_data='buttonE')

    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD], [buttonE]])

    update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из возможных действий',
                              reply_markup=markup)
    return callback

# обработка нажатия клавиш клавиатуры
def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Хотите поздороваться? Введите /hello')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Хотите узнать, что я умею? Нажмите /help"')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Хотите узнать погоду в задданом городе. Введите /w <город>"')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Хотите узнать курс валюты. Введите /c <код валюты>')
    if variant == 'buttonE':
        query.answer()
        query.edit_message_text(text='Хотите произвести арифметическую операцию. Введите /calc <число1 операция число2> Например: 2 + 1')


updater.dispatcher.add_handler(CommandHandler('hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('w', weather_command))
updater.dispatcher.add_handler(CommandHandler('c', currency_command))
updater.dispatcher.add_handler(CommandHandler('start', startCommand))
updater.dispatcher.add_handler(CommandHandler('calc', Calculator))
updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback, pattern=None, run_async=False)
)

print(' server start \n To cancel Ctr + C')
updater.start_polling()
updater.idle()

