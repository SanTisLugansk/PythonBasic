# 1. Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
#    наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# 2. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Vehicle:
    weight = None
    max_speed = None
    engine_power = None
    _owner = None

class Car(Vehicle):
    color = None
    __is_electric = False

    def __init__(self, max_speed, color):
        self.max_speed = max_speed
        self.color = color

    def get_is_electric(self):
        return self.__is_electric

class Airplane(Vehicle):
    maximum_height = None
    range_of_flight = None

class Ship(Vehicle):
    displacement = None

    def __init__(self, weight, max_speed, engine_power, owner=None):
        self.weight = weight
        self.max_speed = max_speed
        self.engine_power = engine_power
        self._owner = owner


my_car = Car(300, 'red')
my_airplane = Airplane()
my_ship = Ship(500, 12, 3000)

print(dir(my_car))
print(my_car.get_is_electric())
print(my_car.weight, my_car.max_speed, my_car.engine_power, my_car.color)
print(my_ship.weight, my_ship.max_speed, my_ship.engine_power, my_ship.displacement)
