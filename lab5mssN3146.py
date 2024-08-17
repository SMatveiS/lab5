import sys
import random


# Проверка на соответствие требованиям к имени файла
def check_file_name(name):
    for i in '\\/:?*<>|+"':
        if i in name:
            sys.stderr.write(f"Ошибка. {name} - недопустимое имя файла\n")
            sys.exit(1)

    if '.' == name[-1] or ' ' == name[-1]:
        sys.stderr.write(f"Ошибка. {name} - недопустимое имя файла\n")
        sys.exit(1)


# Создание файла
def build_file(n, name):
    # Открываем файл для записи
    f = open(name, 'w')
    for i in range(n):
        year = (str(random.randint(0, 2)) + str(random.randint(0, 9)) +
                str(random.randint(0, 9)) + str(random.randint(0, 9)))

        # Первая цифра месяца
        month1 = random.randint(0, 1)
        # Вторая цифра месяца
        if month1 == 0:
            month2 = random.randint(1, 9)
        else:
            month2 = random.randint(0, 2)

        month = str(month1) + str(month2)

        # Создание дня
        # Если в месяце 31 день
        if int(month) in [1, 3, 5, 7, 8, 10, 12]:
            day = str(random.randint(1, 31))
        # Если месяц - февраль
        elif int(month) == 2:
            # Если год високосный
            if int(year) % 4 == 0:
                day = str(random.randint(1, 29))
            else:
                day = str(random.randint(1, 28))
        # Если в месяце 30 дней
        else:
            day = str(random.randint(1, 30))

        # Необходимо, чтобы день состоял из двух цифр
        if len(day) == 1:
            day = '0' + day

        # Генерируем время
        hours = str(random.randint(0, 23))
        if len(hours) == 1:
            hours = '0' + hours

        minutes = str(random.randint(0, 59))
        if len(minutes) == 1:
            minutes = '0' + minutes

        seconds = str(random.randint(0, 59))
        if len(seconds) == 1:
            seconds = '0' + seconds

        # Записываем все данные в формате даты: HH:MM:SS DD.MM.YYYY
        date = f"{hours}:{minutes}:{seconds} {day}.{month}.{year}"
        # Записываем в файл
        f.write(f"{len(date)} {date} ")
    # Закрываем файл
    f.close()

    # Выводим информацию о содержимом файла
    if str(n)[-1] == '1' and str(n)[-2] != '1':
        print(f"Создана {n} строка формата HH:MM:SS DD.MM.YYYY")
    elif str(n)[-1] in '234' and str(n)[-2] != '1':
        print(f"Создано {n} строки формата HH:MM:SS DD.MM.YYYY")
    else:
        print(f"Создано {n} строк формата HH:MM:SS DD.MM.YYYY")
    print("В файле последовательно располагаются размеры строк и сами строки. Строки разделены пробелом.")


# Проверяем количество аргументов
if len(sys.argv) == 1 or len(sys.argv) == 3 or len(sys.argv) > 4:
    sys.stderr.write(f"Ошибка. Напишите: {sys.argv[0]} [-n число] имя_файла\n"
                     f"             или: {sys.argv[0]} -v")
    sys.exit(1)

# Если аргумент '-v'
elif len(sys.argv) == 2 and sys.argv[1] == "-v":
    print("Матвей Сергеевич Смирнов, гр. N3146\n"
          "Вариант: 8-3")

else:
    # Если среди аргументов только имя файла
    if len(sys.argv) == 2:
        # Проверка на соответствие требованиям к имени файла
        check_file_name(sys.argv[1])

        # N - количество объектов в файле
        N = random.randint(10, 1000)

        # Создаём файл
        build_file(N, sys.argv[1])

    # Иначе должна быть задана опция '-n'
    else:
        if sys.argv[1] != '-n':
            sys.stderr.write(f"Ошибка. Напишите: {sys.argv[0]} [-n число] имя_файла\n"
                             f"             или: {sys.argv[0]} -v")
            sys.exit(1)

        for i in sys.argv[2]:
            if i not in '0123456789':
                sys.stderr.write(f"Ошибка. {sys.argv[2]} - не является числом")
                sys.exit(1)

        # Проверка на соответствие требованиям к имени файла
        check_file_name(sys.argv[3])

        # Создаём файл
        build_file(int(sys.argv[2]), sys.argv[3])
