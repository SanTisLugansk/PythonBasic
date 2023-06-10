# 1. Наришіть декоратор, який вимірює час виконання функції
#       робота з часом в python - import time (https://docs.python.org/3/library/time.html#time.time,
#           https://www.programiz.com/python-programming/datetime/current-time)
# 2. Задекоруйте цим декоратором вашу гру з попереднього домашнього завдання

import time
import random

def runtime_meas_decorator(func):
    def function_wrapper(*args, **kwargs):
        #time_start = time.time_ns()        # for some functions the execution time will be = 0
        time_start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        #time_finish = time.time_ns()        # for some functions the execution time will be = 0
        time_finish = time.perf_counter_ns()
        runtime = (time_finish - time_start)/(10**9)
        print(f'{func.__name__}() run for {runtime} sec.')
        return result
    return function_wrapper

# @runtime_meas_decorator         # you can get the execution time of each function
def get_user_choice(prompt1, prompt_next, conformity):
    """
    receiving data from the user, their transformation
    Args:
        prompt1 (str):
        prompt_next (str):
        conformity (Dict):
    Returns:
        (str):
    """
    user_choice = None
    prompt = prompt1
    while user_choice is None:
        user_input = input(prompt)
        user_choice = conformity.get(user_input)
        prompt = prompt_next
    return user_choice

# @runtime_meas_decorator         # you can get the execution time of each function
def get_comp_choise(conformity):
    """
    receiving data from the computer, their transformation
    Args:
        conformity (Dict):
    Returns:
        (str):
    """
    key = str(random.randint(1, len(conformity)))
    return conformity[key]

# @runtime_meas_decorator       # you can get the execution time of each function
def show_result(choise1, choise2):
    """
    getting the result, in terms of the first parameter, outputting the result
    Args:
        choise1 (str):
        choise2 (str):
    Returns:
        None:
    """
    if choise1 == choise2:
        result = 'Draw'
    elif (choise1 == 'rock' and choise2 == 'scissors') or (choise1 == 'paper' and choise2 == 'rock') or (choise1 == 'scissors' and choise2 == 'paper'):
        result = 'You won!'
    else:
        result = 'You lose!'
    print(f'You choise: {choise1}, comp choise: {choise2}')
    print(f'Result: {result}')

@runtime_meas_decorator
def the_game(count=1):
    conformity = {'1': 'rock',
                  '2': 'paper',
                  '3': 'scissors'}

    prompt1 = 'select: '
    for key, value in conformity.items():
        prompt1 += value + ' (' + key + ') or '
    prompt1 += '.'
    prompt1 = prompt1.replace('or .', '---> ')

    prompt2 = 'please enter a valid value ---> '

    for num in range(count):
        user_choise = get_user_choice(prompt1, prompt2, conformity)
        comp_choise = get_comp_choise(conformity)
        show_result(user_choise, comp_choise)

count_str = input('How many times do you want to play? Enter a number ---> ')
try:
    count = int(count_str)
except Exception:
    count = 1
the_game(count)
