# -*- coding: utf-8 -*-

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Factory:
    def __init__(self):
        print('\nЗавод начал свою работу')


class CreateToy(Factory):
    def __init__(self, name, color, type_toy):
        super().__init__()
        self.name = name
        self.color = color
        self.buy_materials()
        self.create(type_toy)
        self.paint()

    def buy_materials(self):
        print('Закупаем материал для', self.name)
        pass

    def create(self, type_toy):
        print('Переходим к изготовлению', type_toy)
        return CreateToy

    def paint(self):
        print('Красим игрушку в {} цвет'.format(self.color))
        pass


test = CreateToy('Продукт №1', 'разноцветный', 'Заяц')

# 2


class Bear(CreateToy):
    pass


class Dog(CreateToy):
    pass


bear = Bear('Продукт №2', 'белый', 'Медведь')
dog = Dog('Продукт №3', 'черный', 'Собака')
