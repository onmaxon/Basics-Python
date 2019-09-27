# -*- coding: utf-8 -*-

from random import randint

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


def generate_list(a, b, n):
    new_list = []
    for i in range(n):
        new_list.append(randint(a, b))
    return new_list


print("\nЗадача 1")

n = 20
# n = int(input("Сколько элементов хотите получить?"))
my_random_list = generate_list(-100, 100, n)
newest_list = []
print(my_random_list)

for i in my_random_list:
    new_elem = i * i
    newest_list.append(new_elem)
print(newest_list)

print("\nЗадача 2")

fruits = ['яблоко', 'киви', 'апельсин', 'груша', 'банан', 'персик']
berries = ['черешня', 'земляника', 'клубника', 'виноград']
print('Первый список: ', fruits)
print('Второе список: ', berries)
cart = fruits.copy()
for i in berries:
    cart.append(i)
print('Общий список: ', cart)

print("\nЗадача 3")

my_random_list = generate_list(-100, 100, n)
print('OLD: ', my_random_list)
new_list = []
for i in my_random_list.copy():
    if int(i % 3) == 0 and i > 0 and i % 4 > 0:
        new_list.append(i)
print('NEW: ', new_list)

