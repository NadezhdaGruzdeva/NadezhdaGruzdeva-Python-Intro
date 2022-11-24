from telegram import Update  #pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler, CallbackContext
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
    items = msg.upper().split() # /sum 123 534543
    currencyCode = items[1]
    update.message.reply_text(f'{Get_currency(currencyCode)}')

updater = Updater(Get_my_Tg_taken())

updater.dispatcher.add_handler(CommandHandler('hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('w', weather_command))
updater.dispatcher.add_handler(CommandHandler('c', currency_command))

print(' server start \n To cancel Ctr + C')
updater.start_polling()
updater.idle()

