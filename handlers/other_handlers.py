import datetime
import math
import requests
from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

@router.message()
async def get_weather(message: Message):
    town = str(message.text)

    try:
        weather_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={town}&lang=ru&units=metric&appid=149abdfa828da7cec13f0cdee4357362", timeout = 1)
        if weather_response.status_code == 200:
            None
        else:
            await message.reply("Плохая связь с сервером.")

        data = weather_response.json()
        city = data["name"]
        cur_temp = data["main"]["temp"]
        feels_temp = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        wind_speed = round(wind)
        if wind_speed < 5:
            w = 'Ветра почти нет'
        elif wind_speed < 10:
            w = 'На улице ветрено'
        elif wind_speed < 20:
            w = 'Ветер очень сильный, будьте осторожны, выходя из дома'
        else:
            w = 'На улице шторм, на улицу лучше не выходить'

        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

        weather_description = data["weather"][0]["main"]

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, я не понимаю, что там за погода..."

        await message.reply(f"{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}\n"
            f"\U000025AAПогода в городе: {city}\n\U000025AAТемпература: {cur_temp}°C \n\U000025AAОщущается как: {feels_temp}°C\n\U000025AA{wd}\n"
            f"\U000025AA{w}\n\U000025AAВлажность: {humidity}%\n\U000025AAДавление: {math.ceil(pressure / 1.333)} мм.рт.ст\n"
            f"Хорошего дня \U0001F495"
            )

    except:
        await message.reply("Проверьте название города или бесы портят связь с сервисом \U0001F622")