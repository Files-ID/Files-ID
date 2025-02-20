import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['document'])
def get_file_id(message):
    file_id = message.document.file_id
    bot.reply_to(message, f"File ID: `{file_id}`", parse_mode="Markdown")

bot.polling(none_stop=True)
