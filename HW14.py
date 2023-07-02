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


# import requests
from requests import get
# import datetime
from datetime import datetime, timedelta


class Date_user:
    date = None
    is_now = False

    def __init__(self):
        # 'Поточного дня буде відображатися офіційний курс гривні до іноземних валют,
        # встановлений НА ЗАВТРА' (https://bank.gov.ua/ua/open-data/api-dev)
        # тому додаємо один день, щоб дата у файлі відповідала датам курсів
        date_now = datetime.now().date() + timedelta(days=1)
        date_str = input('Enter the date in the format "DD.MM.YYYY"  ---> ')
        try:
            self.date = datetime.strptime(date_str, '%d.%m.%Y').date()
        except:
            self.date = date_now

        if self.date == date_now:
            self.is_now = True


class NBU_courses:
    _url_template = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json'
    _url_date_template = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=YYYYMMDD&json'
    _status_code_OK = 200
    _statusRequest_OK = 'OK+%C2%E8%EA%EE%ED%E0%ED%EE'    # = 'OK+Виконано' # Windows-1251 (кирилиця)

    def get_url(self, user_date: Date_user):
        if user_date.is_now:
            url = self._url_template
        else:
            date_str = user_date.date.strftime('%Y%m%d')
            url = self._url_date_template.replace('YYYYMMDD', date_str)
        return url

    def execute_request(self, url):
        res_json = None

        try:
            res = get(url, timeout=3)
        except:
            print('Error getting response to "Get" request')
        else:
            if res.status_code == self._status_code_OK:
                if res.headers.get('statusRequest') == self._statusRequest_OK:
                    res_json = res.json()
                else:
                    print('Returned status request', res.headers.get('statusRequest'))
            else:
                print(f'Returned status code {res.status_code}')
        finally:
            return res_json

    def get_courses(self, user_date: Date_user):
        str_result = ''

        url = self.get_url(user_date)
        # print(url)
        res_json = self.execute_request(url)

        if not res_json is None:
            for el in res_json:
                str_result += f'{(res_json.index(el) + 1)}. {el["cc"]} to UAH: {el["rate"]}\n'

        return str_result


class My_error(Exception):
    message = None

    def __init__(self, arg_message):
        # self.message = arg_message
        self.__class__.message = arg_message

    def __str__(self):
        return f'Error, {self.message}'


# варіант з генерацією винятків, обробка яких має бути зовні
class NBU_courses_with_raise(NBU_courses):
    _date_user = None

    def execute_request(self, url):
        try:
            res = get(url, timeout=3)
        except:
            raise My_error('failed to get a response to the "Get" request')
        else:
            if res.status_code != self._status_code_OK:
                raise My_error(f'returned status code: \'{res.status_code}\'')
            if res.headers.get('statusRequest') != self._statusRequest_OK:
                raise My_error(f'returned status request: \'{res.headers.get("statusRequest")}\'')
            # res.headers.Date - це не дата за яку отримано курси валют, тому перевірка не має сенсу
            # if not self.date_from_headers_is_correct(res.headers):
            #     raise My_error(f'failed to get data for \'{self._date_user.date}\'')

            return res.json()

    def get_courses(self, user_date: Date_user):
        self._date_user = user_date
        str_result = ''

        url = self.get_url(user_date)
        # print(url)
        res_json = self.execute_request(url)

        counter = 0
        for el in res_json:
            if self.date_is_correct(el):
                str_result += f'{(res_json.index(el) + 1)}. {el["cc"]} to UAH: {el["rate"]}\n'
                counter += 1
        print(f'received {counter} courses')

        return str_result

    def date_is_correct(self, element):
        date_str = element["exchangedate"]
        date_course = datetime.strptime(date_str, '%d.%m.%Y').date()
        return (date_course == self._date_user.date)

    def date_from_headers_is_correct(self, headers):
        date_str = headers.get('Date')
        month_table = {'Jan': 1,
                        'Feb': 2,
                        'Mar': 3,
                        'Apr': 4,
                        'May': 5,
                        'Jun': 6,
                        'Jul': 7,
                        'Aug': 8,
                        'Sep': 9,
                        'Oct': 10,
                        'Nov': 11,
                        'Dec': 12}
        try:
            day = int(date_str[5:7])
            month = month_table[date_str[8:11]]
            year = int(date_str[12:16])
            date_from_headers = datetime(year, month, day).date()
            print(date_from_headers)
            return (date_from_headers == self._date_user.date)
        except:
            return False


class Courses_file_txt:
    name = ''

    def __init__(self, user_date: Date_user):
        self.name = f'courses_{user_date.date}.txt'

    def write(self, arg_str):
        try:
            with open(self.name, 'wt') as file:
                 file.write(arg_str)
        except:
            print('An error occurred while writing the file')
        else:
            print(f'File \'{self.name}\' with exchange rates was successfully written')


date_courses = Date_user()
# print(date_courses.date)

# початковий варіант отримання рядка із курсами валют
# my_courses = NBU_courses()
# res_str = my_courses.get_courses(date_courses)
# if len(res_str) > 0:
#     str_write = f' "{date_courses.date.strftime("%d.%m.%Y")}"\n'+res_str
#     # print(f'Str length with courses = {len(str_write)}')

# варіант з генерацією і обробкою виключень, на мій погляд, краще
my_courses = NBU_courses_with_raise()
try:
    res_str = my_courses.get_courses(date_courses)
except My_error:
    print(f'Error: {My_error.message}')
else:
    str_write = f' "{date_courses.date.strftime("%d.%m.%Y")}"\n'+res_str
    # print(f'Str length with courses = {len(str_write)}')

    file_courses = Courses_file_txt(date_courses)
    # print(file_courses.name)
    file_courses.write(str_write)
