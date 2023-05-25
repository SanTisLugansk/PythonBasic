# 1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".

# допускаємо введення від'ємних номерів символів, у цьому випадку рахуємо з кінця введеного слова
# нуль не є допустимим номером символу

word = input('Enter a word --> ')
number_str = input('Enter character number --> ')
if number_str.isdigit():
    index = int(number_str)
    if index == 0:
        print('Zero is not a valid character number')
        index = None
    else:
        index -= 1
elif number_str.find('-') == 0 and number_str[1:].isdigit():
     index = int(number_str)
else:
    print('The entered value is not a number')
    index = None

if type(index) == int:
    if (index >= 0 and index < len(word)) or (index < 0 and -index <= len(word)):
        print(f'The {number_str} symbol in \'{word}\' is \'{word[index]}\'')
    else:
        print('Error: character number out of range')
print('')


# 2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

# вважаємо що символи '.' , ',' , '+' , '=' , послідовність символів ' - ' також, як і будь-який пробіл є роздільниками слів

user_str = input('Enter a string --> ')
my_str = user_str.replace(' - ', ' ')
for char in ".,+=":
  my_str = my_str.replace(char, " ")

user_list = my_str.split()
print(f'There are {len(user_list)} words in the string \'{user_str}\'')
print('')


# 3. Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

list1 = ['1', '2', 3, True, 'False', 5.67, '6', 7, 8, 'Python', -9j, 0, 'Lorem Ipsum']
list2 = []
for list_value in list1:
    # Numeric Types: 	int, float, complex
    #if type(list_value) == int or type(list_value) == float or type(list_value) == complex:
    if type(list_value) == int or type(list_value) == float:    # не враховуємо змінні типу complex
        list2.append(list_value)
print('original list: ', list1)
print('list, containing all values of numeric types: ', list2)
