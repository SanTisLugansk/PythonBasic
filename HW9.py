# Створіть файл lib.py, помістіть в нього функції вашої гри.
# Імпортуйте гру в основний файл і запустіть гру з основного файлу

from lib import the_game as game

count_str = input('How many times do you want to play? Enter a number ---> ')
try:
    count = int(count_str)
except Exception:
    count = 1
game(count)
