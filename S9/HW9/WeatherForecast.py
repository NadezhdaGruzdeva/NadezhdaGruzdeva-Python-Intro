import requests #pip install requests
import datetime
from pprint import pprint # выводит красиво json, раскладывая по полочкам
from mySupersecretToken import Get_my_Tg_taken, Get_my_Weather_taken

# https://www.youtube.com/watch?v=fa1FUW1jLAE&ab_channel=PythonToday

def Get_weather(city, open_weather_token):

    code_to_smile = { #билиотека состояний погоды с эмоджи в значении
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    open_weather_token = Get_my_Weather_taken()
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data) #pprint красиво (не строкой) выводит json 

        city = data["name"] 
        cur_weather = data["main"]["temp"] #из json удобно забирать: как из списков по ключам

        weather_description = data["weather"][0]["main"] #смайлик и описание в зависимости от состояния погоды 
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        return (f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
              f"Хорошего дня!")
              
    except Exception as ex:
        # print(ex)
        return "Проверьте название города"


def main():
    city = input("Введите город: ")
    print(Get_weather(city, Get_my_Weather_taken()))


if __name__ == '__main__':
    main()
    # smile = "\U0001F600"
    # print(smile)

