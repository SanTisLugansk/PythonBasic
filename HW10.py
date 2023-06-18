# 1. Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
#    наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# 2. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class vehicle:
    weight = None
    speed = None
    engine_power = None
    length = None
    width = None
    height = None

class Car(vehicle):
    color = None

class Airplane(vehicle):
    maximum_height = None
    range_of_flight = None

class Ship(vehicle):
    displacement = None
