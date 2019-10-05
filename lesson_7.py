# -*- coding: utf-8 -*-

import random
import sys

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Кажды
	Если цифра есть на карточке - она зачеркивается и й ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""


class RandomNum:
    def __init__(self):
        pass
        # self.number_of_barrel()

    def get_random_num(self):
        return random.randint(1, 91)

    def number_of_barrel(self):
        barrel = [i for i in range(1, 91)]
        random.shuffle(barrel)
        for i, y in enumerate(barrel):
            print('{:*^30}'.format('*'))
            print('Новый бочонок: {} (осталось {})'.format(y, 91 - (i + 1)))
            return y


class Card:
    def __init__(self):
        pass
        # self.generate_new_card()
        # self.write_card('test')

    def _generate_new_card(self):
        new_elem = []
        while len(new_elem) < 5:
            elem = str(RandomNum.get_random_num(self))
            if elem not in new_elem:
                new_elem.append(elem)
        new_elem.sort()
        # new_elem = ' '.join(new_elem)
        return new_elem

    def write_card(self, card_player):
        print('{:-^25}'.format(card_player))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(Card._generate_new_card(card_player)))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(Card._generate_new_card(card_player)))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(Card._generate_new_card(card_player)))
        print('{:-^25}'.format('-'))

    def search(self):
        # TODO Сделать функицию поиска числа в билете.
        pass


class Player(Card):
    def __init__(self, name):
        self.name = name
        self.score = 0


def main():
    num = RandomNum()
    player1 = Player('Ваша карточка')
    player2 = Player('Карточка компьютера')

    while True:
        num.number_of_barrel()
        player1.write_card(player1.name)
        player2.write_card(player2.name)
        inp_user = input('Зачеркнуть цифру? (y/n)')
        if inp_user == 'y':
            # TODO тут должна быть проверка числа
            print('Ищу число в вашем билете!'.upper())
        else:
            print('До свидания')


if __name__ == '__main__':
    main()
