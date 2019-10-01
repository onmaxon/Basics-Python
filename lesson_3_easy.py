# -*- coding: utf-8 -*-

# EASY
# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def where_is_the_user(name, age, city):
    output = '{0}, {1} год(а), проживает в городе {2}'.format(name, age, city)
    print(output)
    return output


def search_max_int(first, second, third):
    int_list = []
    int_list.append(first)
    int_list.append(second)
    int_list.append(third)
    max_int = max(int_list)
    print("Я нашел самое большое число: ", max_int)
    return max_int


def take_many_strings(user_string):
    max_string = (max(user_string, key=len))
    print("Самое длинное слово из введенного текста: ", max_string)
    return max_string


print("__________________\nУровень: easy")

print("\nЗадача 1")
name = input("Ваше имя: ")
age = input("Сколько лет: ")
city = input("В каком городе вы живете: ")
where_is_the_user(name, age, city)

print("\nЗадача 2")
first_int = int(input("Введите первое число: "))
second_int = int(input("Введите второе число: "))
third_int = int(input("Введите третье число: "))
search_max_int(first_int, second_int, third_int)

print("\nЗадача 3")
user_text = input("Текст: ")
string = user_text.split(' ')
take_many_strings(string)
