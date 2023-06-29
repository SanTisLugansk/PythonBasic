# Подключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
# отримайте теперішній курс валют и запишіть його в TXT-файл в такому форматі:
#
#  "[дата, на яку актуальний курс]"
# 1. [назва валюти 1] to UAH: [значення курсу валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу валюти n]
#
# опціонально передбачте для користувача можливість обирати дату, на яку він хоче отримати курс
#
# P.S.  За можливості зробіть все за допомогою ООП


import requests
import datetime


rate_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json'
rate_url_date = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json?date=YYYYMMDD'

date_now = datetime.datetime.now().date()

try:
    res = requests.get(rate_url, timeout=3)
except:
    print('Error getting response to "Get" request')
else:
    if res.status_code == 200:
        # 'OK+%C2%E8%EA%EE%ED%E0%ED%EE' = 'OK+Виконано'     # Windows-1251 (кирилиця)
        if res.headers.get('statusRequest') == 'OK+%C2%E8%EA%EE%ED%E0%ED%EE':
            res_json = res.json()
            str_write = f' "{date_now.strftime("%d.%m.%Y")}"\n'
            for el in res_json:
                str_write += f'{(res_json.index(el) + 1)}. {el["cc"]} to UAH: {el["rate"]}\n'

            file_name = f'{date_now}.txt'
            try:
                with open(file_name, 'wt') as file:
                     file.write(str_write)
            except:
                print('An error occurred while writing the file')
            else:
                print(f'File \'{file_name}\' with exchange rates was successfully written')
        else:
            print('Returned status request', res.headers.get('statusRequest'))
    else:
        print(f'Returned status code {res.status_code}')

