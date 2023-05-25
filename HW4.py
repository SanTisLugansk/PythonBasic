# 1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

# рахуємо також слова, які містять більше двох голосних поспіль

vowel = 'аоуіиеяюєї'

list2 = []
for ch1 in vowel:
    for ch2 in vowel:
        list2.append(ch1 + ch2)

user_str = input('введіть рядок українською мовою --> ')
my_str = user_str.casefold()
my_str = my_str.replace(' - ', ' ')
for char in ".,+=":
    my_str = my_str.replace(char, " ")

words_count = 0
user_list = my_str.split()
for item in user_list:
    if len(item) < 2:
        continue
    for vowel2 in list2:
        if item.find(vowel2) >= 0:
            words_count += 1
            break

print(f'Кількість слів у рядку \'{user_str}\', що містять дві або більше голосних поспіль дорівнює {words_count}')
print('')


# 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
# "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон
# між мінімальною і максимальною ціною.

# магазини, ціни яких дорівнюють граничним, не виводимо на єкран

store_price = {'cito':        47.999,
               'BB_studio':   42.999,
               'momo':        49.999,
               'main-service': 37.245,
               'buy.now':     38.324,
               'x-store':     37.166,
               'the_partner': 38.988,
               'store':       37.720,
               'rozetka':     38.003}
suitable_stores = ''
lower_str = input('введіть мінімальну ціну --> ')
upper_str = input('введіть максимальну ціну --> ')

try:
    lower = float(lower_str)
except Exception:
    lower = None
    print('мінімальна ціна не є числом')

try:
    upper = float(upper_str)
except Exception:
    upper = None
    print('максимальна ціна не є числом')

if (not lower is None) and (not upper is None):
    for key, value in store_price.items():
        if value > lower and value < upper:
            suitable_stores += '"' + key + '"'
    suitable_stores = suitable_stores.replace('""', '", "')
    if len(suitable_stores)>0:
        print(f'Відповіді магазини: {suitable_stores}')
    else:
        print('Немає відповідних магазинів')
