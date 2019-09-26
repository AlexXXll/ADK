import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc' , language='ru')

place = input("В каком городе/стране?: ")

fc = owm.daily_forecast(place, limit=7)

f = fc.get_forecast()

observation = owm.weather_at_place(place)

w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В " + place + "е " + " сейчас " + w.get_detailed_status())

print("Температура сейчас " + str(temp) + "°C")

print("Погода на неделю ")

for weather in f:
	print (weather.get_reference_time('date'),weather.get_detailed_status(),str(weather.get_temperature('celsius')) + "°C")
