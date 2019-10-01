# -*- coding: utf-8 -*-


import os
import shutil
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def create_dirs():
    try:
        n = int(input('Укажите количество новых папок: '))
        for i in range(0, n):
            new_dir = 'dir_' + str(i + 1)
            os.mkdir(new_dir)
            print('Папка {0} создана успешно'.format(new_dir))
    except FileExistsError:
        print('Папка с таким именем: {0} существует!'.format(new_dir))
    except PermissionError:
        print('Не достаточно прав')


def del_dirs():
    try:
        # path_to_dir = '.'
        dirs_to_del = input('Введите папку для удаления : ').split(' ')
        # os.chdir(path_to_dir)
    except FileNotFoundError:
        print('Такой папки не существует')
    for dir in dirs_to_del:
        os.removedirs(dir)
        print('Папка, {}, успешно удалена'.format(dir))


def list_dirs():
    try:
        dirs = [i for i in os.listdir() if os.path.isdir(i)]
        print(dirs)
        return dirs
    except FileNotFoundError:
        print('Такой папки не существует')


def copy_my_script():
    file_name = 'lesson_5_easy.py'
    new_file = file_name + '.bcp'
    if os.path.isfile(file_name):
        shutil.copy(file_name, new_file)
        if os.path.exists(new_file):
            print('Файл , {}, был успешно создан'.format(new_file))
            return True


def move_to_dir(path):
    try:
        os.chdir(path)
        return path
    except FileNotFoundError:
        print('Папка {} не существует!'.format(path))


if 'h' in sys.argv:
    print('справка')
    print('Для удаления папки необходимо ввести имя папок через пробел')
