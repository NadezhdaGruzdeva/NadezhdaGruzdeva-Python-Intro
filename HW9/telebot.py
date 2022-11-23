from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, Updater, CommandHandler, CallbackContext, filters, MessageHandler
import logging
from mySupersecretToken import Get_my_taken
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

# To launch it type in terminal "python telebot.py"
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot

# This part is for setting up logging module, so you will know when (and why) things don't work as expected:
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    The goal is to have this function called every time the Bot receives a Telegram message that contains the /start command. 
    # To accomplish that, you can use a CommandHandler (one of the provided Handler subclasses) and register it in the application
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text= f"Hello, {update.effective_user.first_name}! I'm a prisoner of this bot.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    echo all non-command messages it receives.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    that will take some text as an argument and reply to it in CAPS. To make things easy, 
    you can receive the arguments (as a list, split on spaces) that were passed to a command in the callback function:
    '''
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
    Some confused users might try to send commands to the bot that it doesn't understand, so you can use 
    a MessageHandler with a COMMAND filter to reply to all commands that were not recognized by the previous 
    handlers.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    
    #Here the first real magic happens: You have to create an Application object.
    application = ApplicationBuilder().token(Get_my_taken()).build()
    #The application alone doesn't do anything. To add functionality, we do two things. First, we define a function that should process a specific type of update
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_caps_handler)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    

    # runs the bot until you hit CTRL+C.
    application.run_polling()
