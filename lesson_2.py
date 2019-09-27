# -*- coding: utf-8 -*-

from random import randint


def generate_list(a, b, n):
    new_list = []
    for i in range(n):
        new_list.append(randint(a, b))
    return new_list


print("__________________\nУровень: easy")


fruits = ['яблоко', 'киви', 'апельсин', 'груша', 'банан', 'персик']
print("\nЗадача 1\nДано:", fruits, "\nВывод:")
for i in fruits:
    position = fruits.index(i) + 1
    print('{0}. {1:>8}'.format(position, i))

print("\nЗадача 2")

first_list = generate_list(0, 10, 10)  # [1, 2, 3, 4, 5, 8, 10, 15]
second_list = generate_list(0, 10, 10)  # [5, 3, 5, 10, 8]
print('\nЭто ваш первый список: \n {0}, \nЭто ваш второй список: \n {1}'.format(first_list, second_list))
set1 = set(first_list)
set2 = set(second_list)
b = list(set1 - set2)
print("Я удалил из первого списка повторяющиеся элементы и элементы, присутствующие во втором списке \n", b)

print("\nЗадача 3")

third_list = generate_list(0, 10, 10)
print("Я сгенерировал список:\n", third_list)
update_list = []
for i in third_list:
    if int(i % 2):
        a = i * 2
        update_list.append(a)
        # print('Элемент: {0}, не кратен 2, значит я умножаю его на 2 = {1} '.format(i, a))
    else:
        b = i / 4
        update_list.append(int(b))
        # print('Элемент: {0}, кратен 2, значит я делю его на 4 = {1} '.format(i, int(b)))

print("Вот Ваш новый список:\n", update_list)


print("__________________\nУровень: normal")


print("\nЗадача 1")
lst3 = generate_list(-15, 35, 15)
mod_lst3 = []
print("Сгенерировал список чисел:\n", lst3)
for i in lst3:
    if i >= 0:
        kv = i ** 0.5
        if kv == int(kv):
            mod_lst3.append(int(kv))
print("Квадратные корни элементов исходного списка: ", mod_lst3)

print("\nЗадача 2")
dds = ('первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
       'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
       'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
       'двадцать чертвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
       'двадцать девятое', 'тридцатое', 'тридцать первое')
mms = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
       'декабря')
date = "17.09.2019"
dd, mm, yyyy = date.split('.')
dd = int(dd)
mm = int(mm)
yyyy = int(yyyy)
print(dds[dd-1], mms[mm-1], yyyy, "года")

print("\nЗадача 3")
n = int(input("Сколько элементов хотите получить?"))
my_random_list = generate_list(-100, 100, n)
print("Я сгенерировал Ваш список: ", my_random_list)

print("\nЗадача 4")

print("\na")
lst1 = generate_list(0, 10, 15)
print("Исходный список элементов: ", lst1)
mod_lst1 = set(lst1)
print("Неповторяющиеся элементы исходного списка: ", list(mod_lst1))

print("\nb")
lst2 = generate_list(0, 4, 7)
print("Сгенерировал список чисел:\n", lst2)
mod_lst2 = []
for i in lst2:
    if lst2.count(i) == 1:
        mod_lst2.append(i)
print("Я отобрал только уникальные значения:\n", mod_lst2)

print("__________________\nУровень: hard")

print("\nЗадача 1")
equation = 'y = -12x + 11111140.2121'
x = 2.5
split = equation.split()
var_x = float(split[2].replace('x', '')) * x
y = var_x + float(split[4])
print("Координата опрелена:", y)

print("\nЗадача 2")


days_in_mms = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
date = input("Подскажите мне, какая сегодня дата?: ")
dd, mm, yyyy = date.split('.')
if len(dd) == 2 and len(mm) == 2 and len(yyyy) == 4:
    if 0 < len(mm) <= 12 and 0 < len(yyyy) < 9999 and 0 < len(dd) <= days_in_mms[int(mm)]:
        print("Спасибо, узнать корректную дату всегда приятно!")
    else:
        print("Думаю вы назвали не корректную дату")
else:
    print("Не корректный ввод")

print("\nЗадача 3")

number_of_room = int(input("Номер комнаты: "))

start_room = 1
floor = 1
cube = 1

while number_of_room >= start_room + cube ** 2:
    start_room = start_room + cube ** 2
    floor += cube
    cube += 1

floor += ((number_of_room - start_room) // cube)
room = int((number_of_room - start_room) % cube + 1)

print(floor, room)
