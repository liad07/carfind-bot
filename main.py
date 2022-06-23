from telegram.ext import *
import resposnses as Res

print("Bot started")
def start_command(update, context):
    update.message.reply_text('הזן לוחית רישוי')
def handle_message(update, context):
    text = str(update.message.text).lower()
    resposnses = Res.sample_res(text)
    update.message.reply_text(resposnses)

def main():
    updater = Updater(apikey, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()