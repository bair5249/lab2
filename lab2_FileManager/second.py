import os
import shutil

path = "C:/Users/ASUS/PycharmProjects/pp/lab2_FileManager/WorkingDirectory/"


def one():  # Создание директории
    print("\nВыбрано создание новой папки.")
    name_dir = input("\nВведите назваание директории: ")
    try:
        os.mkdir(path + name_dir)
        print("\nУспех!\n")
    except FileExistsError:
        print("\nТакая папка уже есть!")


def two():  # Удаление директории
    print("\nВыбрано удаление существующей папки")
    name_dir = input("\nВведите назваание директории: ")
    try:
        os.rmdir(path + name_dir)
        print("\nУспех!\n")
    except FileNotFoundError:
        print("\nВы ввели неправильное название, либо такой папки не существует!")


def three():  # Создание файла
    print("\nВыбрано создание пустого .txt файла")
    name_file = input("Введите название файла -> ") + ".txt"
    try:
        open(path + name_file, "w")
        print("\nУспех!\n")
    except FileExistsError:
        print("\nТакой файл уже есть!")


def four():  # Удаление файла
    print("\nВыбрано удаление .txt файла")
    name_file = input("Введите название файла -> ") + ".txt"
    if not os.path.isdir(name_file):
        try:
            os.remove(path + name_file)
            print("\nУспех!")
        except FileNotFoundError:
            print("\nВы ввели неправильное название, либо такой папки не существует!")


def five():  # Переименовывание
    name_1 = input('Введите имя файла: ')
    name_2 = input('Введите новое имя файла: ')
    try:
        if os.path.isdir(path + name_1):
            os.rename(path + name_1, path + name_2)
            print('\nПапка ', name_1, ' переименована на ', name_2)
        elif os.path.isfile(path + name_1 + ".txt"):
            os.rename(path + name_1 + ".txt", path + name_2 + ".txt")
            print('\nФайл ', name_1, ' переименован на ', name_2)
    except FileExistsError:
        print("\nНевозможно переименовать, так как есть объект с таким же именем!\n")


def six():  # Запись текста в файл
    print("\nВыбрана запись текста в файл.")
    name_file = input("\n Укажите имя файла -> ") + ".txt"
    with open(path + name_file, "w") as file:
        file.write(input("\nЧто записываем в файл? \n"))
        file.write("\n")


def seven():  # Просмотр содержимого текстового файла
    print("\nВыбран просмотр содержимого текстового файла.")
    name_file = input("\n Укажите имя файла -> ") + ".txt"
    with open(path + name_file, "r") as file:
        for _ in file:
            print(_)


def eight():
    print("Выбрано копирование из одной папки в другую.")
    previous_dir = path + input("Введите название папки, из которой будет производиться копирование файла ") + "/"
    file_name = previous_dir + input("Введите название файла ") + ".txt"
    dir_name = path + input("Введите название папки, куда хотите переместить файл ")
    try:
        shutil.copy(file_name, dir_name)
    except FileNotFoundError:
        print("Такого файла или директории нет!")


def nine():
    print("Выбрано перемещение одной папки в другую")
    previous_dir = path + input("Введите название папки, из которой будет производиться перемещение файлов ") + "/"
    dir_name = path + input("Введите название папки, куда хотите переместить папку ")
    try:
        shutil.move(previous_dir, dir_name)
    except FileNotFoundError:
        print("Такой папки не существует!")
