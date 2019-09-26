import telebot

bot = telebot.TeleBot("856642659:AAHMG_bDoiASY9-gjL2dG1zBnqJTwSiZJMs")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling( none_stop = True )