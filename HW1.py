# 1. Задача: Створіть дві змінні first = 10, second = 30.
# Виведіть на екран результат математичної взаємодії(+, -, *, / и тд.) для цих чисел.

first = 10
second = 30
print("first = ", first)
print("second = ", second, "\n")
print("first + second =", first + second)
print("first - second =", first - second)
print("second - first =", second - first)
print("first * second =", first * second)
print("first ** second =", first ** second)
print("second ** first =", second ** first)
print("first / second =", first / second)
print("second / first =", second / first)
print("first // second =", first // second)
print("second // first =", second // first)
print("first % second =", first % second)
print("second % first =", second % first, "\n")

# 2. Задача: Створіть змінну і почергово запишіть в неї результат порівняння( <, >, ==, != ) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

compare = False
compare = first < second
print("first < second =", compare)
compare = first > second
print("first > second =", compare)
compare = first == second
print("first == second =", compare)
compare = first != second
print("first != second =", compare, "\n")

# 3. Задача: Створіть змінну - результат конкатенації(складання) строк str1 = "Hello " и str2 = "world".
# Виведіть на екран.

str1 = "Hello "
str2 = "world"
concat_str = str1 + str2
print(concat_str)
