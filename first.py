import lab2_FileManager.second


while True:
    try:
        temp = int(input("Введите цифру того, что вы хотите сделать: \n"
                         "0 - Чтобы выйти \n"
                         "1 - Создать новую папку \n"
                         "2 - Удалить существующую папку \n"
                         "3 - Создать файл .txt \n"
                         "4 - Удалить файл .txt \n"
                         "5 - Переименовать файл или директорию \n"
                         "6 - Запись текста в файл \n"
                         "7 - Чтение текста из файла \n"
                         "8 - Копирование файлов из одной папки в другую \n"
                         "9 - Перемещение одной папки в другую \n"
                         "-> "))
        if temp == 1:
            lab2_FileManager.second.one()
        elif temp == 2:
            lab2_FileManager.second.two()
        elif temp == 3:
            lab2_FileManager.second.three()
        elif temp == 4:
            lab2_FileManager.second.four()
        elif temp == 5:
            lab2_FileManager.second.five()
        elif temp == 6:
            lab2_FileManager.second.six()
        elif temp == 7:
            lab2_FileManager.second.seven()
        elif temp == 8:
            lab2_FileManager.second.eight()
        elif temp == 9:
            lab2_FileManager.second.nine()
        elif temp == 0:
            break
        else:
            print("\nВыберите из списка! \n")

    except ValueError:
        print("\nНужно ввести цифру!")
