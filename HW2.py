# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 6 - вивести повідомлення "Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам пощастить!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
#
# P.S. На екран має бути виведено лише одне повідомлення,
# якщо вік користувача містить цифру тільки відповідне повідомлення!
# Також подумайте над варіантами, коли введені невірні або неадекватні (неможливі) дані.


# Припущення, явно не вказані в завданні:
# значення з дробовою частиною вважається допустимим, але аналізується тільки ціла частина,
# щоб уникнути помилок пов'язаних з неточністью типу float,
# допустимим вважається вік від 0 до 130 років, включно.

age_str = input('Вкажіть Ваш вік: ')

age_str_no_point = age_str.replace('.', '')

# Спочатку введений вік перевіряється на адекватність, так як не можна сказати, що вік містить цифру 7,
# якщо введено 'ук7ц' або '-87', тому що 'ук7ц' або '-87' це не вік
if age_str.count('.') > 1:
    print('Введено не коректне значення віку')
elif age_str.find('-') == 0 and age_str_no_point[1:].isdigit():
    print('Вік не може бути від\'ємним')
elif not age_str_no_point.isdigit():      # elif age_str_no_point.isdigit() == False:
    print('Необхідно ввести число')
else:
    age_float = float(age_str)
    age = int(age_float)
    if age > 130:
        print('Вік не може бути більшим за 130 років')
    # якщо вік користувача містить цифру тільки відповідне повідомлення!,
    # тому ця умова перша, коли введено адекватні дані
    elif str(age).find('7') >= 0:
        print('Вам пощастить!')
    elif age < 6:
        print('Де твої батьки?')
    elif age < 16:
        print('Це фільм для дорослих!')
    elif age > 65:
        print('Покажіть пенсійне посвідчення!')
    else:
        print('А білетів вже немає!')

# Думаю, що всі повідомлення мають виводитися однією мовою,
# оскільки в завданні явно вказані повідомлення українською,
# то українська використовується для всіх повідомлень
