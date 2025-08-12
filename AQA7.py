#Задача 1 (Работа с файлами)
#Создай текстовый файл numbers.txt и запиши в него числа от 1 до 10, каждое с новой строки.
from os import write

#Метод 1
with open("numbers.txt", "w") as file:
    file.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")

#Метод 2
with open("numbers.txt", "w") as file:
    for number in range(1, 11):
        file.write(f"{number}\n")

#Следующая задача (№2) — Чтение файла
#Прочитай содержимое файла numbers.txt (который ты только что создал) и выведи его построчно в консоль.

#Метод 1
with open("numbers.txt", "r") as file:
    for line in file:
        print(line.strip())

#Метод 2
with open("numbers.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

#Следующая задача (№3) — Контекстный менеджер и запись
#Дан список строк:

#fruits = ["apple", "banana", "orange"]
#Задача:

#Открой файл fruits.txt в режиме записи ("w").

#Запиши каждый фрукт из списка в файл с новой строки.

#Используй контекстный менеджер with.

fruits = ["apple", "banana", "orange"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(f"{fruit}\n")

#Следующая задача (№4) - Чтение и обработка данных
#Есть файл data.txt с содержимым:

#text
# 10
# 15
# 20
# 25
# 30
#Задача:

#Открой файл data.txt в режиме чтения

#Прочитай все числа из файла

#Вычисли и выведи их сумму

total = 0
with open("data.txt", "r") as file:
    for line in file:
        try:
            total += int(line.strip())
        except ValueError:
            continue
print(f"Сумма чисел: {total}")


#Задача 5 (Простая работа с файлами)
#Есть файл greeting.txt с одной строкой:

#text
#Hello
#Задача:

#Открой файл greeting.txt в режиме чтения

#Прочитай его содержимое

#Допиши в этот же файл строку , world! (чтобы в итоге получилось Hello, world!)

#Используй режим r+ для чтения и записи одновременно

filename = "greeting.txt"
with open(filename, "w+") as f:  # w+ - режим записи и чтения
    f.write("Hello, Python!")
    f.seek(0)  # возвращаемся в начало файла
    print(f.read())

#Следующая задача (№6) - Простая работа с файлами
#Задача:

#Создай файл months.txt

#Запиши в него названия первых трёх месяцев года (каждое с новой строки):

#text
#January
#February
#March
#Требования:

#Используй контекстный менеджер with

#Режим записи "w"

#Каждый месяц с новой строки

#Метод 1
with open("months.txt", "w") as file:
    file.write("January\nFebruary\nMarch")

#Метод 2
months = ["January", "February", "March"]
with open("months.txt", "w") as file:
    for month in months:
        file.write("{month}\n")

#Следующая задача (№7) - Чтение и обработка
#Задача:

#Прочитай файл months.txt, который ты только что создал

#Выведи все месяцы в консоль в обратном порядке (сначала March, потом February, потом January)

#Метод 1
with (open("months.txt", "r") as file):
    lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())

#Метод 2
with open("months.txt", "r") as file:
    lines = file.readlines()
    for line in lines[::-1]:  # [::-1] создает перевернутую копию списка
        print(line.strip())

#Решение с нумерацией:

with open("months.txt", "r") as file:
    months = file.readlines()

    for index, month in enumerate(reversed(months), start=1):
        print(f"{index}. {month.strip()}")

#Задача 1 (Работа с файлами)
#Создай текстовый файл notes.txt и запиши в него две строки:

#text
#Первая строка
#Вторая строка
#Требования:

#Используй контекстный менеджер with

#Файл должен быть создан в той же папке, где находится скрипт

with open("notes.txt", "w") as file:
    file.write("Первая строка\nВторая строка")

#Задача 2 (Контекстный менеджер with)
#Есть файл data.txt с содержимым:

#text
#10
#20
#30
#Задача:
#Прочитай все числа из файла, вычисли их сумму и запиши результат в новый файл sum.txt.

#Требования:

#Используй два контекстных менеджера with (один для чтения, другой для записи)

#Не забудь преобразовать строки в числа (int())

#Убедись, что в sum.txt будет только одно число (сумма)

total = 0
with open("data.txt", "r") as file:
    for line in file:
        try:
            # Если строка содержит только число
            number = int(line.strip())
            total += number
        except ValueError:
            # Если строка не является числом (например, содержит дату и текст)
            print(f"Пропускаем строку: {line.strip()}")
            continue

with open("sum.txt", "w") as file:
    file.write(str(total))


#Задача 3 (Работа с файлами)
#Создай файл colors.txt и запиши в него названия трёх цветов, каждое слово в отдельной строке:

#text
#red
#green
#blue
#Требования:

#Используй контекстный менеджер with

#Запись должна быть выполнена одним вызовом file.write() (с переносами строк \n)

#Файл должен создаваться заново при каждом запуске скрипта

with open("colors.txt", "w") as file:
    file.write("red\ngreen\nblue")


#Задача 4 (Контекстный менеджер with)
#Есть файл log.txt с содержимым:

#text
#2023-01-01: Старт системы
#2023-01-02: Ошибка 404
#2023-01-03: Восстановление
#Задача:
#Добавь в конец файла новую запись:
#2023-01-04: Завершение работы

#Требования:

#Используй режим добавления ("a" или "a+")

#Не изменяй существующие строки

#Примени контекстный менеджер with

with open("log.txt", "a") as file:
    file.write("\n2023-01-04: Завершение работы")

#Задача 5 (Упрощённая версия)
#Создай файл hello.txt и запиши в него одну строку:
#"Привет, мир!"

#Требования:

#Используй with open()

#Режим записи — "w"

#Только одна строка в файле

with open("hello.txt", "w") as file:
    file.write("Привет, мир!")

#Следующая супер-простая задача (№6):
#Создай файл numbers.txt и запиши в него числа от 1 до 5 через запятую (без пробелов):

with open("numbers.txt", "w") as file:
    file.write("1,2,3,4,5")

#Следующая простая задача (№7):
#Прочитай файл numbers.txt (который ты только что создал) и выведи его содержимое в консоль.

#Требования:

#Используй with open()

#Режим чтения — "r"

#Вывод должен быть точно таким: 1,2,3,4,5 (без кавычек)

with open("numbers.txt", "r") as file:
    content = file.read()
    print(content.strip())

#Задача 8 (Работа с файлами)
#Создай файл animals.txt и запиши в него 3 любимых животных, каждое с новой строки.

#Требования:

#Используй только один вызов file.write()

#Режим записи — "w"

#Формат файла:

#text
#кошка
#собака
#попугай

with open("animals.txt", "w") as file:
    file.write("кошка\nсобака\nпопугай")

#Следующая простая задача (№9):
#Прочитай файл animals.txt и выведи первое животное из списка.
#Требования:
#Используй with open()
#Режим чтения — "r"
#Вывод должен быть: Первое животное: кошка

with open("animals.txt", "r") as file:
    first = file.readline().strip()
    print(f"Первое животное: {first}")

#Задача 1 (Работа с файлами + with)
#Прочитай файл numbers.txt, в котором записаны числа (каждое с новой строки), и выведи сумму всех чисел.
#Требования:
#Используй with open()
#Режим чтения — "r"
#Файл содержит только числа (по одному в строке)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        # Пробуем разделить по запятым если есть
        numbers = line.split(',')
        for num in numbers:
            try:
                total += int(num)
            except ValueError:
                print(f"Пропускаем нечисловое значение: '{num}'")
print(total)

#Задача 2 (Работа с файлами + запись)
#Создай новый файл squares.txt и запиши в него квадраты чисел от 1 до 10 (каждое число с новой строки).
#Требования:
#Используй with open()
#Режим записи — "w"
#Формат содержимого файла:

with open("squares.txt", "w") as file:
    for number in range(1,11):
        file.write(f"{number**2}\n")

#Задача 3 (Чтение и обработка данных)
#В файле data.txt записаны строки с информацией о товарах в формате:
#название,количество,цена
#(например: Яблоки,10,50)

#Задание:
#Напиши программу, которая:

#Читает файл data.txt

#Вычисляет общую стоимость каждого товара (количество × цену)

#Записывает результат в новый файл total.txt в формате:
#название: общая_стоимость
#(например: Яблоки: 500)

with open("data.txt", "r") as file:
    lines = file.readlines()  # читаем все строки

with open('total.txt', 'w') as output_file:
    for line in lines:  # обрабатываем КАЖДУЮ строку
        line = line.strip()  # убираем пробелы и переносы строк
        if not line:  # пропускаем пустые строки
            continue

        try:
            parts = line.split(',')
            name = parts[0]
            quantity = int(parts[1])
            price = int(parts[2])
            total = quantity * price
            output_file.write(f"{name}: {total}\n")
        except (ValueError, IndexError):
            print(f"Ошибка в строке: {line}. Пропускаем.")


# Задача 1 (Создание и запись в файл)
# Создай файл hello.txt и запиши в него строку: "Привет, мир!". Используй контекстный менеджер with.

with open("hello.txt", "w") as file:
    file.write("Привет, мир!")

# Задача 2 (Чтение файла)
# Прочитай и выведи содержимое файла hello.txt (из предыдущей задачи) с помощью with.

with open("hello.txt", "r") as file:
    print(file.read())

# Задача 3 (Добавление текста в файл)
# Дополни файл hello.txt строкой: "Это новая строка." без удаления предыдущего содержимого.

with open("hello.txt", "a") as file:
    file.write("\nЭто новая строка.")

# Задача 4 (Проверка существования файла)
# Проверь, есть ли файл secret.txt в текущей папке. Выведи:
# "Файл найден" — если он существует,
# "Файл отсутствует" — если нет.

try:
    with open("secret.txt", "r") as file:
        print("Файл найден")
except FileNotFoundError:
    print("Файл отсутствует")


# Задача 1 (Работа с файлами)
# Создай файл numbers.txt и запиши в него числа от 1 до 10, каждое с новой строки

with open("numbers.txt", "w") as file:
    for number in range(1, 11):
        file.write(f"{number}\n")

# Задача 2 (Контекстный менеджер with)
# Создай файл greeting.txt и используя конструкцию with,
# запиши в него строку "Hello, Python!". Затем прочитай содержимое этого файла и выведи его в консоль.

with open("greeting.txt", "w") as file:
    file.write("Hello, Python!")

with open("greeting.txt", "r") as file:
    print(file.read())

# Задача 8 (Работа с файлами и исключениями)
# Дан файл mixed_data.txt с содержимым:
# text
# 10
# hello
# 25
# 42
# world
# 7
# Задача:
# Откройте файл в режиме чтения
# Прочитайте все строки
# Найдите и выведите сумму только числовых строк (игнорируя нечисловые)
# Запишите результат в файл sum_numbers.txt

with open("mixed_data.txt", "w") as file:
    file.write("10\nhello\n25\n42\nworld\n7")

total = 0

with open("mixed_data.txt", "r") as file:
    for line in file:
        try:
            total += int(line.strip())
        except ValueError:
            continue

with open("sum_numbers.txt", "w") as file:
    print(f"Сумма чисел: {total}")
    file.write(f"Сумма чисел: {total}")

# Задача 1 (Работа с файлами)
# Напиши код, который создает текстовый файл numbers.txt и записывает в него числа от 1 до 10,
# каждое число на новой строке.

with open("numbers.txt", "w") as file:
    for number in range(1,11):
        file.write(f"{number}\n")

with open("numbers.txt", "w") as file:
    file.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n")

# Задача 2 (Контекстный менеджер with)
# Есть файл notes.txt с текстом:
#
# Купить хлеб
# Позвонить маме
# Заправить кровать
# Напиши код, который добавляет новую задачу "Выучить Python" в конец файла, не удаляя старые записи.

# 1. Создаем файл и текст
with open("notes.txt", "w") as file:
    file.write("Купить хлеб\nПозвонить маме\nЗаправить кровать\n")

# 2. Записываем данные по условию задачи
with open("notes.txt", "a") as file:
    file.write("Выучить Python")

# 3. Проверка результата
with open("notes.txt", "r") as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)

# Задача 3 (Построчный вывод)
# Файл tasks.txt содержит:
#
# Закончить проект
# Сделать зарядку
# Полить цветы
# Задание:
# Напиши код, который выводит каждую задачу из файла с нумерацией, например:

# 1. Создаем файл и текст
with open("tasks.txt", "w") as file:
    file.write("Закончить проект\nСделать зарядку\nПолить цветы\n")

# 2.
with open("tasks.txt", "r") as file:
    print("Задачи дня:")
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")

# Проверь себя
# Попробуй без подсказок написать код, который:
# Создаёт файл shopping.txt с 3 покупками.
# Добавляет 4-ю покупку.
# Выводит список с нумерацией.
# Если получится — тема освоена! Если нет — вернёмся к примерам.

# 1. Создаем файл и записываем текст
with open("shopping.txt", "w") as file:
    file.write("Джинсы\nФутболка\nОбувь\n")

# 2. Добавляем в конец 4 строку
with open("shopping.txt", "a") as file:
    file.write("Ветровка\n")

# 3. Нумеруем строки и выводим конечный результат
with open("shopping.txt", "r") as file:
    print("Необходимо купить:")
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")