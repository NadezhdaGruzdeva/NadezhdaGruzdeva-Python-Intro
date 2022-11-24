from telegram import Update  #pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
# from spy import *
from mySupersecretToken import Get_my_Tg_taken, Get_my_Weather_taken
from WeatherForecast import Get_weather

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
 update.message.reply_text(f'/hi\n/time\n/help')
def time_command(update: Update, context: CallbackContext):
 log(update, context)
 update.message.reply_text(f'{datetime.datetime.now().time()}')
def sum_command(update: Update, context: CallbackContext):
 log(update, context)
 msg = update.message.text
 print(msg)
 items = msg.split() # /sum 123 534543
 city = items[1]
 update.message.reply_text(f'{Get_weather(city, Get_my_Weather_taken())}')



updater = Updater(Get_my_Tg_taken())
updater.dispatcher.add_handler(CommandHandler('hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start')
updater.start_polling()
updater.idle()

