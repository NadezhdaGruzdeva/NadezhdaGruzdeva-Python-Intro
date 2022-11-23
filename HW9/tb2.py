from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from mySupersecretToken import Get_my_taken

#The filters module contains a number of so-called filters that filter incoming messages for text, images, 
# status updates and more. Any message that returns True for at least one of the filters passed to 
# MessageHandler will be accepted.
...

#will take some text as an argument and reply to it in CAPS. 
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    
if __name__ == '__main__':
    application = ApplicationBuilder().token(Get_my_taken()).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()