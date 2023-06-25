# Доопрацюйте класс Triangle зі свого попереднього дз.
#  1.  Реалізуйте перевірку даних на те що вершини є Point за допомогою property.
#  2.  Реалізуйте ітератор по вершинам трикутника


from math import sqrt
# from HW11 import Point as Point, Line as Line
from HW11 import Point, Line


class Triangle:
    _apex_a = Point(0, 0)
    _apex_b = Point(0, 0)
    _apex_c = Point(0, 0)
    _changed = False
    _area = None

    apex_a = property()
    apex_b = property()
    apex_c = property()

    current_apex = None     # у остаточній версії не використовується

    @apex_a.getter
    def apex_a(self):
        return self._apex_a

    @apex_a.setter
    def apex_a(self, value):
        if isinstance(value, Point):
            if self._apex_a != value:
                self._apex_a = value
                self._changed = True
        else:
             raise TypeError

    @apex_b.getter
    def apex_b(self):
        return self._apex_b

    @apex_b.setter
    def apex_b(self, value):
        if isinstance(value, Point):
            if self._apex_b != value:
                self._apex_b = value
                self._changed = True
        else:
             raise TypeError

    @apex_c.getter
    def apex_c(self):
        return self._apex_c

    @apex_c.setter
    def apex_c(self, value):
        if isinstance(value, Point):
            if self._apex_c != value:
                self._apex_c = value
                self._changed = True
        else:
             raise TypeError

    def __init__(self, arg_apex_a, arg_apex_b, arg_apex_c):
        self.apex_a = arg_apex_a
        self.apex_b = arg_apex_b
        self.apex_c = arg_apex_c

    def __str__(self):
        return f'Triangle with apex: {self.apex_a}, {self.apex_b}, {self.apex_c}'

    # у такому вигляді працює тільки якщо немає вкладених циклів for
    # def __iter__(self):
    #     self.current_apex = self.__class__.current_apex
    #     return self
    #
    # def __next__(self):
    #     if id(self.current_apex) == id(self.apex_a):
    #         self.current_apex = self.apex_b
    #     elif id(self.current_apex) == id(self.apex_b):
    #         self.current_apex = self.apex_c
    #     elif id(self.current_apex) == id(self.apex_c):
    #         raise StopIteration
    #     else:
    #         self.current_apex = self.apex_a
    #
    #     return self.current_apex

    def __iter__(self):
        return Triangle_iterator(self)

    def area(self, round_to=None):
        # короткочасні змінні можуть мати імена з однієї або двох літер, це говорить про 'тимчасовість' змінної,
        # формула площі читаеється легше при використанні коротких імен
        if self._changed:
            print('calculate the area')
            ab = Line(self.apex_a, self.apex_b).length()
            bc = Line(self.apex_b, self.apex_c).length()
            ca = Line(self.apex_c, self.apex_a).length()
            s = (ab + bc + ca) / 2
            self._area = sqrt(s * (s - ab) * (s - bc) * (s - ca))
            self._changed = False

        if isinstance(round_to, int):
            return round(self._area, round_to)
        else:
            return self._area


class Triangle_iterator:
    triangle = None
    current_apex = None

    def __init__(self, triangle):
        self.triangle = triangle

    # iтератор повинен повертати self у методі __iter__
    def __iter__(self):
        return self

    def __next__(self):
        if id(self.current_apex) == id(self.triangle.apex_a):
            self.current_apex = self.triangle.apex_b
        elif id(self.current_apex) == id(self.triangle.apex_b):
            self.current_apex = self.triangle.apex_c
        elif id(self.current_apex) == id(self.triangle.apex_c):
            raise StopIteration
        else:
            self.current_apex = self.triangle.apex_a

        return self.current_apex


p1 = Point(0, 2)
p2 = Point(1, 3)
p3 = Point(3, 9)
# print(p1, p2, p3)

my_triangle = Triangle(p1, p2, p3)
print(f'Area {my_triangle} = {my_triangle.area(3)}')
print(f'Area {my_triangle} = {my_triangle.area(3)}')

my_triangle.apex_a = Point(2, 10)
print(f'Area {my_triangle} = {my_triangle.area(3)}\n')

for i in my_triangle:
    print(i)
    for j in my_triangle:
        print(f' --- inner loop --- {j}')
