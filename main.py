import telebot
import os
import sys

# جلب التوكن من متغيرات البيئة
TOKEN = os.getenv("BOT_TOKEN")

# التحقق من وجود التوكن
if not TOKEN:
    print("Error: BOT_TOKEN not found in environment variables.")
    sys.exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['document'])
def get_file_id(message):
    file_id = message.document.file_id
    bot.reply_to(message, f"File ID: `{file_id}`", parse_mode="Markdown")

bot.polling(none_stop=True)
