import telebot

bot = telebot.TeleBot("6145320852:AAGuREUNxcj7PjFGi0zyXgXP-GoDAUWJVrw")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)
	#bot.reply_to(message, message.text)
        
bot.infinity_polling()
