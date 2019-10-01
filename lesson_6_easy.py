# -*- coding: utf-8 -*-

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TownCar:           # Название класса
    def __init__(self, car_model, speed, color, is_police):
        self.model = car_model
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self._driver()

    def go(self):        # Метод
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула на', direction)

    def _driver(self):
        print('\nВодитель машины: {} сел за руль.'.format(self.model))

    def get_serial_number(self):
        return self._serial_number


class SportCar:
    def __init__(self, car_model, speed, color, is_police):
        self.model = car_model
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self._driver()

    def go(self):        # Метод
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула на', direction)

    def _driver(self):
        print(self.model, 'водитель за рулем')

    def get_serial_number(self):
        return self._serial_number


class WorkCar:
    def __init__(self, car_model, speed, color, is_police):
        self.model = car_model
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self._driver()

    def go(self):        # Метод
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def _driver(self):
        print(self.model, 'водитель за рулем')


class PoliceCar:
    def __init__(self, car_model, speed, color, is_police):
        self.model = car_model
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self._driver()

    def go(self):        # Метод
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def _driver(self):
        print(self.model, 'водитель за рулем')


my_car = TownCar('VW', 90, 'красный', False)
print('\nМодель машины: {}, цвет: {}, скорость: {} км/ч, полицейская ли это машина: {}'.format(my_car.model, my_car.color, my_car.speed, my_car.is_police))
my_car.go()
my_car.turn('лево')
my_car.stop()


# Задача - 2


class Car(TownCar):
    pass


police_car = Car('Ford', 110, 'черно-белая', True)
print('\nМодель машины: {}, цвет: {}, скорость: {} км/ч, полицейская ли это машина: {}'.format(police_car.model, police_car.color, police_car.speed, police_car.is_police))
police_car.go()
police_car.turn('право')
police_car.stop()
