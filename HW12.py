# Доопрацюйте класс Triangle зі свого попереднього дз.
#  1.  Реалізуйте перевірку даних на те що вершини є Point за допомогою property.
#  2.  Реалізуйте ітератор по вершинам трикутника


from math import sqrt
from HW11 import Point as Point, Line


class Triangle:
    _apex_a = Point(0, 0)
    _apex_b = Point(0, 0)
    _apex_c = Point(0, 0)
    _changed = False
    _area = None

    apex_a = property()
    apex_b = property()
    apex_c = property()

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

    # def __init__(self, arg_apex_a, arg_apex_b, arg_apex_c):
    #     if isinstance(arg_apex_a, Point) and isinstance(arg_apex_b, Point) and isinstance(arg_apex_c, Point):
    #         self.apex_a = arg_apex_a
    #         self.apex_b = arg_apex_b
    #         self.apex_c = arg_apex_c
    #     else:
    #         raise TypeError

    def __init__(self, arg_apex_a, arg_apex_b, arg_apex_c):
        self.apex_a = arg_apex_a
        self.apex_b = arg_apex_b
        self.apex_c = arg_apex_c

    def __str__(self):
        return f'Triangle with apex: {self.apex_a}, {self.apex_b}, {self.apex_c}'

    def area(self, round_to=None):
        # короткочасні змінні можуть мати імена з однієї або двох літер, це говорить про 'тимчасовість' змінної,
        # формула площі читаеється легше при використанні коротких імен
        if self._changed:
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

p1 = Point(0, 0)
p2 = Point(0, 13)
p3 = Point(3.693, 14.539)
print(p1, p2, p3)

almost_triangle_Heron = Triangle(p1, p2, p3)
print(f'Area {almost_triangle_Heron} = {almost_triangle_Heron.area(3)}')