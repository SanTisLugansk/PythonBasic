# Доопрацюйте гру з заняття наступним чином:
# Додайте вибір слова з будь-якого джерела на ваш вибір
# Додайте лічильник спроб вгадати слово і вихід з цтклу по переповненню лічильника
# Додайте більш інформативні повідомлення (список можливих букв для введення,
# повідомлення про невірне введення, повідомлення про кількість спроб що залишилися і тд)
# Опційно. Додайте можливість повторювати гру. Запитати в гравця чи хоче він повторити гру Yes/No
# і повторювати якщо він введе Yes, завершити якщо введе No

import random
word_list = ['Hello', 'world', 'strip', 'Enter', 'counter', 'result', 'Guess']
answer = 'Yes'

while answer == 'Yes':
    word = random.choice(word_list).lower()

    guess_result = '?' * len(word)
    guessed_letters = []
    entered_letters = set()
    counter = len(word) * 2

    available_letters = 'abcdefghijklmnopqrstyuwxvz'
    print(f'Guess the word: {guess_result}, you can use such letters:', available_letters)

    while guess_result != word and counter > 0:

        user_letter = input(f'Attempts left: {counter}. Enter the letter: ').lower()
        counter -= 1
        additional_message = 'Try again!' if counter > 0 else ''

        if len(user_letter) > 1:
            print('Too long!', additional_message)
            continue
        elif len(user_letter) < 1:
            print('Too short!', additional_message)
            continue
        elif user_letter not in available_letters:
            print('Unavailable!', additional_message)
            continue
        elif user_letter in entered_letters:
            print('Duplicate!', additional_message)
            continue
        else:
            entered_letters.add(user_letter)

        if user_letter in word:
            guessed_letters.append(user_letter)
            guess_result = ''
            for char in word:
                guess_result += char if char in guessed_letters else '?'
            message = 'The word is:' if guess_result == word else 'Guess the word:'
            print(message, guess_result)
        else:
            print(f'The letter \'{user_letter}\' is not in the word.', additional_message)

    if guess_result == word:
        print('Congratulations!')
    else:
        print('Ended up trying')

    answer = input('Enter "Yes", if you want to repeat the game. --> ').lower().capitalize()

print('Have a good day')