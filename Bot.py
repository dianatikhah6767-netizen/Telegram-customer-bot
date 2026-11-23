import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! به واحد پشتیبانی خوش آمدید. چطور می‌توانم کمکتان کنم؟")

@bot.message_handler(func=lambda message: True)
def answer(message):
    bot.reply_to(message, "پیام شما دریافت شد. همکاران ما به‌زودی پاسخ‌گوی شما خواهند بود.")

bot.infinity_polling()
