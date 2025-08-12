#Задача 1 (Создание функций)
#Напиши функцию greet(), которая выводит в консоль "Привет, мир!".

def greet():
    print("Привет, мир!")


greet()

#Задача 2 (Аргументы функций)
# Напиши функцию multiply(a, b), которая возвращает произведение двух чисел a и b.

def multiply(a, b):
    return a*b


result = multiply(5, 8)
print(result)

#Задача 3 (Возвращение данных из функций)
#Напиши функцию is_even(number), которая:
#Принимает целое число number,
#Возвращает True, если число чётное, и False — если нечётное.

def is_even(number):
    return number % 2 == 0


result = is_even(7)
print(result)

#Задача 4 (Дефолтные аргументы)
#Напиши функцию greet_user(name), где name по умолчанию "Гость". Она должна возвращать "Привет, {name}!".

def greet_user(name="Гость"):
    return f"Привет, {name}!"


print(greet_user())
print(greet_user("tito_artist"))

#Задача 1 (Создание и вызов функций)
#Напиши функцию print_hello, которая просто выводит в консоль строку "Hello!". Затем вызови эту функцию.

def print_hello():
    print("Hello!")

print_hello()

#Задача 2 (Аргументы функций)
#Напиши функцию multiply, которая принимает два числа a и b и выводит их произведение.

def multiply(a, b):
    print(a*b)


multiply(10, 3)


#Задача 3 (Аргументы с дефолтными значениями)
#Напиши функцию greet(name), которая принимает имя и выводит "Привет, {name}!".
#Если имя не передано, пусть по умолчанию будет "Гость"

def greet(name="Гость"):
    return f"Привет, {name}!"


print(greet())
print(greet("Artist"))

#Задача 4 (Возвращение данных из функций)
#Напиши функцию is_even(num), которая принимает число и возвращает True, если оно чётное, и False — если нечётное.

def is_even(num):
    return num % 2 == 0


print(is_even(5))

#Задача 1.
#Напиши функцию say_hello(), которая не принимает аргументов и выводит строку "Привет, мир!". Затем вызови эту функцию.
#Требования:
#Функция должна быть определена через def.
#Вызов функции — отдельной строкой.

def say_hello():
    print("Привет, мир!")


say_hello()

#Задача 2.
#Напиши функцию greet(name), которая:
#Принимает один аргумент name (строка),
#Выводит сообщение "Привет, {name}!" (используй f-строку).

def greet(name):
    print(f"Привет, {name}!")


greet("Анна")

#Задача 3.
#Напиши функцию order(coffee, size='medium'), которая:
#Принимает обязательный аргумент coffee (название напитка)
#Принимает необязательный аргумент size со значением по умолчанию 'medium'
#Выводит строку: "Ваш заказ: {size} {coffee}"

def order(coffee, size='medium'):
    print(f"Ваш заказ: {size} {coffee}")


order("латте")
order("капучино", "large")

#Задача 4.
#Напиши функцию multiply(a, b), которая:
#Принимает два числа a и b,
#Возвращает (не выводит!) их произведение.

def multiply(a, b):
    return a * b


result = multiply(5, 7)
print(result)

#Задача 5.
#Напиши декоратор verbose, который:
#Принимает функцию
#Перед вызовом функции выводит: "Вызываю функцию {имя_функции}"
#После вызова выводит: "Функция {имя_функции} выполнена"

def verbose(func):

    def wrapper(*args, **kwargs):

        print(f"Вызываю функцию {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} выполнена")
        return result

    return wrapper

@verbose
def say_hello():
    print("Привет")

say_hello()

# 1. Функции в Python (создание и вызов)
# Задача 1. Напиши функцию say_weather(), которая выводит в консоль: "Сегодня солнечно!".

def say_weather():
    print("Сегодня солнечно!")


say_weather()

# 2. Аргументы функций
# Задача 2. Напиши функцию multiply(a, b), которая возвращает произведение чисел a и b.

def multiply(a, b):
    return a * b


result = multiply(5, 15)
print(result)

# 3. Аргументы с дефолтными значениями
# Задача 3. Напиши функцию greet(name), где name по умолчанию "Гость".
# Функция должна возвращать строку "Привет, {name}!".

def greet(name="Гость"):
    return f"Привет, {name}!"


print(greet())

# 4. Возвращение данных из функций
# Задача 4. Напиши функцию is_positive(num), которая возвращает True,
# если число положительное, и False — если нет.

def is_positive(num):
    if num >= 0:
        return True

    else:
        return False

print(is_positive(-8))

# 5. Декораторы
# Задача 5. Напиши декоратор log_call, который выводит:
# "Функция {имя_функции} вызвана" перед вызовом функции.

def log_call(func):

    def wrapper(*args, **kwargs):

        print(f"Функция {func.__name__} вызвана")
        result = func(*args, **kwargs)
        return result

    return wrapper

@log_call
def say_hello():
    print("Привет")

say_hello()

# Первая задача (Декораторы):
# Напиши декоратор repeat, который вызывает декорируемую функцию 2 раза подряд.

def repeat(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper

@repeat
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Следующая задача (Декораторы):
# 2. Напиши декоратор uppercase, который переводит результат функции в верхний регистр.

def uppercase(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).upper()
        return result

    return wrapper

@uppercase
def get_message():
    return "hello, world!"

print(get_message())

# Задача 3 (Декораторы с аргументами)
# Напиши декоратор repeat(n), который вызывает декорируемую функцию N раз (N задаётся при вызове декоратора).

def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator

@repeat(3)  # Вызывает функцию 3 раза
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Задача 4 (Простой декоратор-логгер)
# Напиши декоратор logger, который выводит:
# "Функция начинается" перед вызовом функции.
# "Функция завершена" после вызова.

def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Функция начинается")
        func(*args, **kwargs)
        print(f"Функция завершена")

    return wrapper

@logger
def say_hello(name):
    print(f"Привет, {name}!")

say_hello("Анна")

# Задача 1: Декоратор-счётчик
# Напиши декоратор count_calls, который считает, сколько раз вызвали функцию, и выводит это число после каждого вызова.

def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        func(*args, **kwargs)
        count += 1
        print(f"Всего вызовов: {count}")

    return wrapper

@count_calls
def greet(name):
    print(f"Привет, {name}!")

greet("Анна")  # Вывод: Привет, Анна! (Всего вызовов: 1)
greet("Пётр")  # Вывод: Привет, Пётр! (Всего вызовов: 2)

# Задача 2: Декоратор для проверки аргументов
# Напиши декоратор check_positive, который проверяет, что все числовые аргументы функции положительные.
# Если нет — выводит "Ошибка: аргумент должен быть > 0".

def check_positive(func):

    def wrapper(*args, **kwargs):
        for arg in args:
             if isinstance(arg, (int, float)) and arg <= 0:
                 return f"Ошибка: аргумент должен быть > 0"

        # Проверяем именованные аргументы (kwargs)
        for arg in kwargs.values():
             if isinstance(arg, (int, float)) and arg <= 0:
                 return f"Ошибка: аргумент должен быть > 0"

        return func(*args, **kwargs)

    return wrapper

@check_positive
def multiply(a, b):
    return a * b

print(multiply(5, 3))   # Выведет: 15
print(multiply(-2, 10)) # Выведет: Ошибка: аргумент должен быть > 0

# Задача 1 (Функции в Python / Создание и вызов функций)
# Напиши функцию greet(), которая не принимает аргументов
# и просто печатает в консоль строку "Hello, Python!". Затем вызови эту функцию.

def greet():
    print("Hello, Python!")


greet()

# Задача 2 (Аргументы функций)
# Напиши функцию multiply(a, b), которая принимает два числа a и b и возвращает их произведение.
# Вызови функцию с аргументами 3 и 5, затем выведи результат в консоль.
# (Проверь: передаются ли аргументы в функцию, верно ли организован возврат результата.)

def multiply(a, b):
    return a * b

print(multiply(5, 12))

# Задача 3 (Аргументы с дефолтными значениями)
# Напиши функцию welcome(name, greeting="Hello"), которая принимает имя (name)
# и опциональный аргумент greeting (значение по умолчанию — "Hello").
# Функция должна возвращать строку в формате: "{greeting}, {name}!".
#
# Пример вызова:
# welcome("Alice") → вернет "Hello, Alice!",
# welcome("Bob", "Hi") → вернет "Hi, Bob!".

def welcome(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(welcome("Alice"))
print(welcome("Bob", "Hi"))

# Задача 4 (Возвращение данных из функций)
# Напиши функцию is_even(num), которая принимает число num и возвращает True,
# если число чётное, и False — если нечётное. Вызови функцию с числами 4 и 7, выведи результаты в консоль.

def is_even(num):
    return num % 2 == 0


print(is_even(4))
print(is_even(7))

# Задача 5 (Декораторы)
# Напиши декоратор uppercase_decorator, который преобразует результат функции в верхний регистр.

def uppercase_decorator(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"

print(say_hello())  # Должно вывести: "HELLO, WORLD!"

# Задача 6 (Функции в Python / Комбинированная)
# Напиши функцию calculate(x, y, operation), где:
# x, y — числа,
# operation — строка "+", "-", "*", или "/".
# Функция должна возвращать результат выбранной операции или None, если операция неизвестна.
# Пример:
# calculate(10, 2, "+") → 12,
# calculate(5, 3, "?") → None.

def calculate(x, y, operation):

    if operation == "+":
        return x + y

    elif operation == "-":
        return x - y

    elif operation == "*":
        return x * y

    elif operation == "/":
        if y == 0:
            return "Ошибка: деление на ноль запрещено"
        return x / y

    else:
        return None

print(calculate(10, 2, "+"))
print(calculate(10, 2, "-"))
print(calculate(10, 2, "*"))
print(calculate(10, 2, "/"))
print(calculate(10, 0, "/"))
print(calculate(5, 3, "?"))

# Задача 7 (Аргументы функций / Значения по умолчанию)
# Напиши функцию create_user(email, username=None):
# Если username не передан, функция должна использовать часть до @ из email как имя пользователя.
# Возвращает словарь вида {"email": email, "username": username}.

def create_user(email, username=None):
    if username is None:
        if '@' in email:
            username = email.split('@')[0]
        else:
            username = "default_username"
    return {"email": email, "username": username}


print(create_user("test@mail.com"))
print(create_user("alice@site.com", "Alice"))

# Задача 8 (Базовая)
# Напиши функцию format_name(first_name, last_name, middle_name=None), которая:
# Если middle_name не указано, возвращает строку "First: {first}, Last: {last}"
# Если указано, возвращает "First: {first}, Middle: {middle}, Last: {last}"

def format_name(first_name, last_name, middle_name=None):
    if middle_name is None:
        return f"First: {first_name}, Last: {last_name}"
    else:
        return f"First: {first_name}, Middle: {middle_name}, Last: {last_name}"


print(format_name("Artem", "Lutfullin"))
print(format_name("Artem", "Lutfullin", "Rinatovich"))

# Задача 9 (С проверкой условий)
# Напиши функцию get_credentials(email, password, username=None, country="RU"), которая:
# Если username не указан, берёт часть email до @ (как в предыдущей задаче)
# Всегда проверяет, что пароль длиннее 6 символов (иначе возвращает None)
# Добавляет страну в результат

def get_credentials(email, password, username=None, country="RU"):
    if username is None:
        if '@' in email:
            username = email.split('@')[0]
        else:
            username = "default_username"

    if len(password) >= 6:
        return {
            "email": email,
            "password": password,
            "username": username,
            "country": country
        }
    else:
        return None

print(get_credentials("test@mail.com", "qwertyu"))
print(get_credentials("test@mail.com", "qwertyu", "Artist", "USA"))

# Задача 10 (Комбинированная)
# Создай функцию parse_coordinates(coords, default_z=0), которая:
# Принимает строку в формате "x,y,z" (например, "10,20,30") или "x,y"
# Возвращает словарь {"x": int, "y": int, "z": int}
# Если z не указан, использует default_z
# Если строка некорректна, возвращает None

def parse_coordinates(coords, default_z=0):
    parts = coords.split(',')

    if len(parts) == 2:
        try:
            x = int(parts[0])
            y = int(parts[1])
            return {"x": x, "y": y, "z": default_z}
        except ValueError:
             return None

    elif len(parts) == 3:
        try:
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            return {"x": x, "y": y, "z": z}
        except ValueError:
            return None

    else:
        return None

print(parse_coordinates("10,20"))
print(parse_coordinates("5,10,15"))
print(parse_coordinates("abc,def"))
print(parse_coordinates("1,2,3,4"))



