import telebot
from telebot import types

bot = telebot.TeleBot('5940664174:AAEX6wiHCnS1qjZZCmbThtg_PEazi4lntjk')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()