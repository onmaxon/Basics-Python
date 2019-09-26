# -*- coding: utf-8 -*-

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')
    print("ping - тестовый ключ")

def check_system():
    # TODO Сделать определение оперционной системы
    pass

def check_par(argument):
    try:
        key = argument[1]
        param = argument[2]
    except IndexError:
        param = None
    if key:
        if do.get(key):
            do[key](param)
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")


def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file(file_name):
    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    if not os.path.isfile(file_name):
        print('Файл {} не существует'.format(file_name))
    if os.path.isfile(file_name):
        new_file = file_name + '.bcp'
        if os.path.exists(new_file):
            print('Файл {} уже существует'.format(new_file))
        else:
            shutil.copy(file_name, new_file)
            print("Файл ", new_file, " был успешно создан")


def del_file(del_name):
    if not del_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    if os.path.isfile(del_name):
        answer = input('Точно хотите удалить файл, {}\n (Y/N): '.format(del_name))
        if answer == 'Y' or answer == 'y':
            os.remove(del_name)
            print('Файл {} успешно удален'.format(del_name))
        else:
            pass
    else:
        print('Файл {} не существует'.format(del_name))


def move_to(move_dir):
    if not move_dir:
        print('Необходимо указать путь вторым параметром')
        return
    if os.path.isdir(move_dir):
        os.chdir(move_dir)
        a = os.getcwd()
        print('Переходим', a)


def pwd():
    # TODO Доделать
    if not pwd:
        print('Необходимо указать имя папки вторым параметром')
        return
    os.getcwd()
    print('Путь к папке: ', os.getcwd(pwd))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "cd": move_to,
    "ls": pwd,
}

check_par(sys.argv)
