import pyowm
from pyowm.exceptions import api_response_error

import time

import telebot


owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc',
 language='ru')
bot = telebot.TeleBot(
	"856642659:AAHMG_bDoiASY9-gjL2dG1zBnqJTwSiZJMs")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Join casinoXXX")
	time.sleep(2)
	bot.send_message(message.chat.id, "Шучу, напиши в каком городе тебя погода интересует?")

@bot.message_handler(content_types=['text'])
def send_echo(msg):
	try:
		message = msg.text
		fc = owm.daily_forecast(message, limit=7)

		f = fc.get_forecast()

		observation = owm.weather_at_place(message)

		w = observation.get_weather()

		temp = w.get_temperature('celsius')["temp"]

	except api_response_error.NotFoundError:
		bot.reply_to(message, "Не братка, это не город,\n а видимо набор бессвязных символов.\n Ты шо в двоичном коде набираешь название города?\n Отдохни 5 сек)\n")
		time.sleep(5)

	res = ""
	res += "В " + message + "е " + " сейчас " \
	+ w.get_detailed_status()
	res += "\nТемпература сейчас " + str(temp) + "°C"
	res += "\nПогода на неделю\n" 
	res += ''.join([weather.get_reference_time('date').strftime("%d-%b-%Y (%H:%M:%S.%f)") + 
		weather.get_detailed_status() + 
		str(weather.get_temperature('celsius')) + "°C\n"\
		 for weather in f])

	bot.reply_to(msg, res)

bot.polling( none_stop = True )