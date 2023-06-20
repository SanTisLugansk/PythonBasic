# 1. Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати
#    тільки обʼєкти класу int або float
# 2. Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати
#    тільки обʼєкти класу Point
# 3. Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
#    Реалізуйте перевірку даних, аналогічно до класу Line.
#    Визначет метод, що містить площу трикутника.
#    Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)
#    s = (a + b + c) / 2
#    A = sqrt (s * (s - a) * (s - b) * (s - c))

import math

a = 4
b = 13
c = 15

s = (a + b + c) / 2
A = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(A)