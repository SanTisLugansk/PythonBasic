# Доопрацюйте класс Triangle зі свого попереднього дз.
#  1.  Реалізуйте перевірку даних на те що вершини є Point за допомогою property.
#  2.  Реалізуйте ітератор по вершинам трикутника


from math import sqrt
from copy import copy
from HW11 import Point, Line


class Triangle:
    _apex_a = Point(0, 0)
    _apex_b = Point(0, 0)
    _apex_c = Point(0, 0)
    _area = None
    _area_apex_a = None
    _area_apex_b = None
    _area_apex_c = None

    apex_a = property()
    apex_b = property()
    apex_c = property()

    @apex_a.getter
    def apex_a(self):
        return self._apex_a

    @apex_a.setter
    def apex_a(self, value):
        if isinstance(value, Point):
            self._apex_a = value
        else:
             raise TypeError

    @apex_b.getter
    def apex_b(self):
        return self._apex_b

    @apex_b.setter
    def apex_b(self, value):
        if isinstance(value, Point):
            self._apex_b = value
        else:
             raise TypeError

    @apex_c.getter
    def apex_c(self):
        return self._apex_c

    @apex_c.setter
    def apex_c(self, value):
        if isinstance(value, Point):
            self._apex_c = value
        else:
             raise TypeError

    def __init__(self, arg_apex_a, arg_apex_b, arg_apex_c):
        self.apex_a = arg_apex_a
        self.apex_b = arg_apex_b
        self.apex_c = arg_apex_c

    def __str__(self):
        return f'Triangle with apex: {self.apex_a}, {self.apex_b}, {self.apex_c}'

    def __iter__(self):
        return Triangle_iterator(self)

    def area(self, round_to=None):
        # короткочасні змінні можуть мати імена з однієї або двох літер, це говорить про 'тимчасовість' змінної,
        # формула площі читаеється легше при використанні коротких імен
        is_changed = False
        if self._apex_a != self._area_apex_a:
            self._area_apex_a = copy(self._apex_a)
            is_changed = True
        if self._apex_b != self._area_apex_b:
            self._area_apex_b = copy(self._apex_b)
            is_changed = True
        if self._apex_c != self._area_apex_c:
            self._area_apex_c = copy(self._apex_c)
            is_changed = True

        if is_changed:
            # print('calculate the area')
            ab = Line(self.apex_a, self.apex_b).length()
            bc = Line(self.apex_b, self.apex_c).length()
            ca = Line(self.apex_c, self.apex_a).length()
            s = (ab + bc + ca) / 2
            self._area = sqrt(s * (s - ab) * (s - bc) * (s - ca))

        if isinstance(round_to, int):
            return round(self._area, round_to)
        else:
            return self._area


class Triangle_iterator:
    triangle = None
    current_apex_name = None

    def __init__(self, triangle):
        self.triangle = triangle
        self.current_apex_name = None

    # iтератор повинен повертати self у методі __iter__
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_apex_name is None:
            self.current_apex_name = 'apex_a'
        elif self.current_apex_name == 'apex_a':
            self.current_apex_name = 'apex_b'
        elif self.current_apex_name == 'apex_b':
            self.current_apex_name = 'apex_c'
        else:
            raise StopIteration

        return self.triangle.__getattribute__(self.current_apex_name)


p1 = Point(0, 0)
p2 = Point(1, 8)
p3 = Point(3, 4)
# print(p1, p2, p3)

my_triangle = Triangle(p1, p2, p3)
print(f'Area {my_triangle} = {my_triangle.area(3)}\n')

for i in my_triangle:
    print(i)
    i.x = i.x * 2
    # print(f'Area {my_triangle} = {my_triangle.area(3)}')

    for j in my_triangle:
        print(f' --- inner loop --- {j}')
        j.y = int(j.y / 2)

    print(f'Area {my_triangle} = {my_triangle.area(3)}\n')
