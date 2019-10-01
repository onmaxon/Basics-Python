# -*- coding: utf-8 -*-

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.

# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _attack(self):
        return self.damage

    def defence(self, damage):
        dial_damage = damage / self.armor
        health_after_attack = (self.health - dial_damage)
        self.health = health_after_attack
        print('{} получает {} урона, здоровья осталось: {}'.format(self.name, round(dial_damage), round(health_after_attack)))

    def get_attack(self):
        return self._attack()


class Enemy(Person):
    def personal_info(self):
        return self.health


class Player(Person):
    def personal_info(self):
        return self.health


class Round:
    def run_game(self, who_attack, who_defence):
        game_round = 1
        while who_defence.health > 0 or who_attack.health > 0:
            print('Раунд №', game_round)
            who_attack.get_attack()
            who_defence.defence(who_attack.damage)
            who_defence.get_attack()
            who_attack.defence(who_defence.damage)
            game_round += 1
            if who_defence.health <= 0:
                print('\nИгра окончена.\n{} проиграл'.format(who_defence.name))
                break
            elif who_attack.health <= 0:
                print('\nИгра окончена.\n{} проиграл'.format(who_attack.name))
                break


gamers = {'player': {'name': 'Max',
                     'health': 100,
                     'damage': 30,
                     'armor': 1.9},
          'enemy': {'name': 'Bot',
                    'health': 100,
                    'damage': 30,
                    'armor': 1.2}
          }

player = Player(gamers['player']['name'], gamers['player']['health'], gamers['player']['damage'], gamers['player']['armor'])
enemy = Enemy(gamers['enemy']['name'], gamers['enemy']['health'], gamers['enemy']['damage'], gamers['enemy']['armor'])

game = Round()
game.run_game(player, enemy)
