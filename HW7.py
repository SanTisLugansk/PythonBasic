# Напишіть гру "Rock paper scissors" https://en.wikipedia.org/wiki/Rock_paper_scissors
# Грають гравець і компʼютер. Вdід даних гравцем - через input()
# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
# Не забувайте що кожна функція має виконувати тільки одне завдання
# і про правила написання коду (DRY, KISS, YAGNI).

import random

def get_prompt_string(conformity):
    """
    generates a prompt string for user input, based on the keys and values of the received Dict
    Args:
        conformity (Dict):
    Returns:
        (str):
    """
    prompt = 'select: '
    for key, value in conformity.items():
        prompt += value + ' (' + key + ') or '
    prompt += '.'
    prompt = prompt.replace('or .', '---> ')
    return prompt

def get_user_input(prompt_string):
    """
    gets the prompt string, returns the data entered by the user
    Args:
        prompt_string (str):
    Returns:
        (str):
    """
    return input(prompt_string)

def check_user(user_input, conformity):
    """
    checks the correctness of the received data, if the data is correct, then they are converted
    Args:
        user_input (str):
        conformity (Dict):
    Returns:
        (str|None):
    """
    return conformity.get(user_input)

def get_user_choice(prompt1, prompt_next, conformity):
    """
    receiving data from the user, checking the correctness of the received data,
    their transformation
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
        input_str = get_user_input(prompt)
        user_choice = check_user(input_str, conformity)
        prompt = prompt_next
    return user_choice

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

def get_result1(choise1, choise2):
    """
    getting the result, in terms of the first parameter
    Args:
        choise1 (str):
        choise2 (str):
    Returns:
        (str):
    """
    if choise1 == choise2:
        return 'Draw'
    elif (choise1 == 'rock' and choise2 == 'scissors') or (choise1 == 'paper' and choise2 == 'rock') or (choise1 == 'scissors' and choise2 == 'paper'):
        return 'You won!'
    else:
        return 'You lose!'

def show_result(choise1, choise2):
    """
    getting the result, in terms of the first parameter, outputting the result
    Args:
        choise1 (str):
        choise2 (str):
    Returns:
        None:
    """
    result = get_result1(choise1, choise2)
    print(f'You choise: {choise1}, comp choise: {choise2}, result: {result}')


conformity = {'1': 'rock',
              '2': 'paper',
              '3': 'scissors'}

prompt1 = get_prompt_string(conformity)
prompt2 = 'please enter a valid value ---> '

for num in range(5):
    user_choise = get_user_choice(prompt1, prompt2, conformity)
    comp_choise = get_comp_choise(conformity)
    show_result(user_choise, comp_choise)
