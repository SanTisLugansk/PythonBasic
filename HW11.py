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

class Point:
    x_coord = 0
    y_coord = 0

    def __init__(self, x, y):
        # check type (int, float)
        self.x_coord = x
        self.y_coord = y

    def __str__(self):
        return f'Point {self.x_coord} {self.y_coord}'

    def __getitem__(self, item):
        print(f'__getitem__ {item}')
        if item == 0:
            return self.x_coord
        elif item == 1:
            return self.y_coord
        else:
            raise TypeError

    def __setitem__(self, item, value):
        print(f'__setitem__ {item}, {value}')
        if item == 0:
            self.x_coord = value
        elif item == 1:
            self.y_coord = value
        else:
            raise TypeError

    def __eq__(self, other):
        # check type Point
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord


class Line:
    begin_point = None
    end_point = None

    def __init__(self, begin, end):
        # check type Point
        self.begin_point = begin
        self.end_point = end

    def __str__(self):
        return f'Line from [{self.begin_point}] to [{self.end_point}]'

    def length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord
        return math.sqrt(k1 ** 2 + k2 ** 2)

    def __len__(self):
        """ len(obj) """
        return 2

    def __contains__(self, item):
        """ a in b """
        print('__contains__', item)
        return self.begin_point == item or self.end_point == item


a = 4
b = 13
c = 15

s = (a + b + c) / 2
A = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(A)