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

from math import dist, sqrt


class Point:
    x = 0
    y = 0
    # не бажано використовувати однолітерні атрибути, але в завданні вказано 'атрибути x та y'

    def __init__(self, arg_x, arg_y):
        if isinstance(arg_x, (float, int)) and isinstance(arg_y, (float, int)):
            self.x = arg_x
            self.y = arg_y
        else:
            raise TypeError

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __getitem__(self, item):
        print(f'__getitem__ {item}')
        if isinstance(item, int):
            if item == 0:
                return self.x
            elif item == 1:
                return self.y
            else:
                raise IndexError
        else:
            raise TypeError

    def __setitem__(self, item, value):
        print(f'__setitem__ {item}, {value}')
        if isinstance(item, int) and isinstance(value, (float, int)):
            if item == 0:
                self.x = value
            elif item == 1:
                self.y = value
            else:
                raise IndexError
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError

    def __ne__(self, other):
        # print(f'Point __ne__ type(other) =', type(other))
        if isinstance(other, Point):
            return self.x != other.x or self.y != other.y
        else:
            raise TypeError

    def list(self):
        return [self.x, self.y]
    # хотілося за допомогою MAGIC METHOD зробити так, щоб вираз '[объект_класса_Point]' повертав '[x, y]',
    # тобто, щоб при створенні списку з об'єкта класу Point,
    # створювався список, що містить координати x і y цього об'єкта, але не вийшло (не знаю як)


class Line:
    begin = None
    end = None

    def __init__(self, begin, end):
        if isinstance(begin, Point) and isinstance(end, Point):
            self.begin = begin
            self.end = end
        else:
            raise TypeError

    def __str__(self):
        return f'Line({self.begin} - {self.end})'

    def length(self, round_to=None):
        result = dist(self.begin.list(), self.end.list())
        if isinstance(round_to, int):
            return round(result, round_to)
        else:
            return result

    def __contains__(self, item):
        """ a in b """
        print('__contains__', item)
        if isinstance(item, Point):
            return self.begin == item or self.end == item
        else:
            raise TypeError


class Triangle:
    apex_a = None
    apex_b = None
    apex_c = None

    def __init__(self, arg_apex_a, arg_apex_b, arg_apex_c):
        if isinstance(arg_apex_a, Point) and isinstance(arg_apex_b, Point) and isinstance(arg_apex_c, Point):
            self.apex_a = arg_apex_a
            self.apex_b = arg_apex_b
            self.apex_c = arg_apex_c
        else:
            raise TypeError

    def __str__(self):
        return f'Triangle with apex: {self.apex_a}, {self.apex_b}, {self.apex_c}'

    def area(self, round_to=None):
        # короткочасні змінні можуть мати імена з однієї або двох літер, це говорить про 'тимчасовість' змінної,
        # формула площі читаеється легше при використанні коротких імен
        ab = Line(self.apex_a, self.apex_b).length()
        bc = Line(self.apex_b, self.apex_c).length()
        ca = Line(self.apex_c, self.apex_a).length()
        s = (ab + bc + ca) / 2
        result = sqrt(s * (s - ab) * (s - bc) * (s - ca))
        if isinstance(round_to, int):
            return round(result, round_to)
        else:
            return result

if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(0, 13)
    p3 = Point(3.693, 14.539)
    # print(p1, p2, p3)

    # a = Line(p1, p2)    # 13
    # b = Line(p2, p3)    # 4
    # c = Line(p3, p1)    # 15
    # print(a, b, c)
    # print(a.length(2), b.length(2), c.length(2))

    almost_triangle_Heron = Triangle(p1, p2, p3)
    print(f'Area {almost_triangle_Heron} = {almost_triangle_Heron.area(3)}')
