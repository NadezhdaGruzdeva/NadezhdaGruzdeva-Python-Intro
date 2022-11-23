from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5888622101:AAGxBKPt8RtQiFKKIHazNTyv2e0CW--M8D4").build()

app.add_handler(CommandHandler("hello", hello))
print("server start")
app.run_polling()