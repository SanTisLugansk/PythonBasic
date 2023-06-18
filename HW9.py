# Створіть файл lib.py, помістіть в нього функції вашої гри.
# Імпортуйте гру в основний файл і запустіть гру з основного файлу

import lib

count_str = input('How many times do you want to play? Enter a number ---> ')
try:
    count = int(count_str)
except Exception:
    count = 1
lib.the_game(count)
