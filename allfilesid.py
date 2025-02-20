import telebot

TOKEN = "7900346127:AAH0u02C1Q8grdXxNIyMn2sYcvL630itCLU"  # ضع التوكن الخاص بالبوت هنا
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['document'])
def get_file_id(message):
    file_id = message.document.file_id
    bot.reply_to(message, f"File ID: `{file_id}`", parse_mode="Markdown")

bot.polling(none_stop=True)
