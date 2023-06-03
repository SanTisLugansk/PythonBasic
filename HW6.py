# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
#    Якщо перетворити не вдається функція має повернути 0.

def  my_float(num):
    try:
        return float(num)
    except Exception:
        return 0

str1 = input('Введіть щось --> ')
print(my_float(str1))


# 2. Напишіть функцію, що приймає два аргументи. Функція повинна
#    a. якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#    b. якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
#    c. у будь-якому іншому випадку повернути кортеж з цих аргументів

# input() завжди повертає str, тому створимо функцію для визначення типу введених даних
def cast_to_type(str_arg):
    if str_arg == 'None':
        return None
    elif str_arg == 'True':
        return True
    elif str_arg == 'False':
        return False
    else:
        try:
            return int(str_arg)
        except Exception:
            try:
                return float(str_arg)
            except Exception:
                return str_arg

def two_arguments(arg1, arg2):
    if (type(arg1) == int or type(arg1) == float) and (type(arg2) == int or type(arg2) == float):
        return arg1 * arg2
    elif type(arg1) == str and type(arg2) == str:
        return arg1+arg2
    else:
        return (arg1, arg2)

str2 = input('Введіть ще щось --> ')

print(two_arguments(cast_to_type(str1), arg2=cast_to_type(str2)))


# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
#    a. Попросіть користувача ввести свсвій вік.
#       - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
#       - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
#       - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
#       - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
#       - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
#    b. Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
#       Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача
#       (1 - рік, 22 - роки, 35 - років і тд...).
#       Наприклад:  "Тобі ж 5 років! Де твої батьки?"
#                   "Вам 81 рік? Покажіть пенсійне посвідчення!"
#                   "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"

def input_age():
    age_str = input('Вкажіть Ваш вік: ')
    age_str_no_point = age_str.replace('.', '')

    if age_str.count('.') > 1:
        print('Введено не коректне значення віку')
    elif age_str.find('-') == 0 and age_str_no_point[1:].isdigit():
        print('Вік не може бути від\'ємним')
    elif not age_str_no_point.isdigit():  # elif age_str_no_point.isdigit() == False:
        print('Необхідно ввести число')
    else:
        age_float = float(age_str)
        age = int(age_float)
        if age > 130:
            print('Вік не може бути більшим за 130 років')
        else:
            return age
    return None

def correct_form_word(num):
    Modulus = num%10
    if Modulus == 1:
        return 'рік'
    elif Modulus == 2 or Modulus == 3 or Modulus == 4:
        return 'роки'
    else:
        return 'років'

def display_message(age):
    if age is None:
        return
    else:
        message_age = str(age) + ' ' + correct_form_word(age)
        if str(age).find('7') >= 0:
            print(f'Вам {message_age}, вам пощастить')
        elif age < 7:
            print(f'Тобі ж {message_age}! Де твої батьки?')
        elif age < 16:
            print(f'Тобі лише {message_age}, а це е фільм для дорослих!')
        elif age > 65:
            print(f'Вам {message_age}? Покажіть пенсійне посвідчення!')
        else:
            print(f'Незважаючи на те, що вам {message_age}, білетів всеодно нема!')

numeric = input_age()
display_message(numeric)
