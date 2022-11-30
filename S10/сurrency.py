import requests #pip install requests
import datetime
from pprint import pprint # выводит красиво json, раскладывая по полочкам
from mySupersecretToken import Get_my_Tg_taken, Get_my_Weather_taken


def Get_currency(valute):
    try:
        r = requests.get(
            f"https://www.cbr-xml-daily.ru/daily_json.js"
        )
        data = r.json()
        # pprint(data) #pprint красиво (не строкой) выводит json 

        # valute_inp = input('Введите трехзначное обозначение валюты, курс которой вы хотите узнать.\n'\
            # 'Например USD, EUR или CNY\n').upper()
        valuteName = data['Valute'] [valute] ["Name"]
        valuteNominal = data['Valute'] [valute] ["Nominal"]
        valuteValue = data['Valute'] [valute] ["Value"]

        return (f'Текущий курс ЦБ РФ: {valuteValue} рублей за {valuteNominal} единиц(у) {valuteName}.')
              
    except Exception as ex:
        # print(ex)
        return "Проверьте условное обозначение валюты"


def main():
    valute_inp = input('Введите трехзначное обозначение валюты, курс которой вы хотите узнать.\n'\
            'Например USD, EUR или CNY\n').upper()
    print(Get_currency(valute_inp))


if __name__ == '__main__':
    main()
    # smile = "\U0001F600"
    # print(smile)

