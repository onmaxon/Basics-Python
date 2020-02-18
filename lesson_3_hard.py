# -*- coding: utf-8 -*-

print("__________________\nУровень: hard")

# HARD
# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.

# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
# Сохраните эти сущности, полностью, каждую в свой файл
# в качестве названия для файла использовать name, расширение .txt

# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,

# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


def read_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        line = file.readlines()
        player_conf = {}
        for i in line:
            data = i.replace('\n', '').split(' - ')
            player_conf[data[0]] = data[1]
        print(player_conf)
        return player_conf


def write_in_file(user):
    file = open(user['name'] + '.txt', 'w', encoding='utf-8')
    for key, value in user.items():
        file.write(key + ' - ' + str(value) + '\n')
    file.close()


def dial_damage():
    total_damage = player['damage'] / enemy['armor']
    return total_damage


def attack(person1, person2, total_damage):
    combat = {'health': person2['health'] - total_damage}
    person2.update(combat)
    print('После нападения персонажем {0}, у защищающегося персонажа {1} осталось - {2} hp'.format(person1['name'].upper(), person2['name'].upper(), person2['health']))


# user_name = input('Введите имя вашего персоонажа: ')
#enemy_name = input('Введите имя вашего врага: ')
#
#player = {'name': user_name, 'health': 100, 'damage': 50, 'armor': 1.2}
# write_in_file(player)
#
#enemy = {'name': enemy_name, 'health': 100, 'damage': 50, 'armor': 1.2}
#write_in_file(enemy)
#
# attack(player, enemy, dial_damage())
# answer = input("If you want to load config of your player: ")
# if answer == 'yes':
#     config = input("Set name of config:")
# else:
#     pass

# read_file('1.txt')
# read_file('2.txt')
# attack(player_conf, read_file('2.txt'), dial_damage())
# while True:
#     attack(read_file('1.txt'), read_file('2.txt'), dial_damage())
#     attack(read_file('2.txt'), read_file('1.txt'), dial_damage())




