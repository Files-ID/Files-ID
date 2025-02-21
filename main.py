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

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "مرحبًا! قم برفع الملف الذي ترغب في الحصول على file_id الخاص به.")

# التعامل مع الملفات المرفوعة من قبل المستخدم
@bot.message_handler(content_types=['document'])
def handle_uploaded_file(message):
    # استخراج file_id من الملف المرسل
    file_id = message.document.file_id
    
    # إرسال file_id للمستخدم بعد رفع الملف
    bot.reply_to(message, f"تم رفع الملف بنجاح! File ID: `{file_id}`", parse_mode="Markdown")

bot.polling(none_stop=True)
