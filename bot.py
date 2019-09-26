import time

import pyowm
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
	message = msg.text
	fc = owm.daily_forecast(message, limit=7)

	f = fc.get_forecast()

	observation = owm.weather_at_place(message)

	w = observation.get_weather()

	temp = w.get_temperature('celsius')["temp"]

try:
    owm.weather_at_place(place)
except pyowm.exceptions.api_response_error.NotFoundError
    res """Не братка, это не город, а видимо набор бессвязных символов, ты шо в двоичном коде набираешь название города? Отдохни 5 сек)"""
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