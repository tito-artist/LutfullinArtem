# Задача 1 (Арифметические операции)
# Напиши код, который вычисляет сумму, разность, произведение и частное двух переменных a = 10 и b = 2.
# Результаты выведи в формате:
# Сумма: X, Разность: Y, Произведение: Z, Частное: W.

a = 10
b = 2

addition = a+b
subtraction = a-b
multiplication = a*b
dividing = a/b
print ("Сумма:", addition)
print ("Разность:", subtraction)
print ("Произведение:", multiplication)
print ("Частное:", dividing)

# Задача 2 (Типы данных)
# Напиши код, который создаёт переменные:
# num (число 5),
# text (строка "Python"),
# is_active (логическое значение True),
# а затем выводит их типы данных в формате:
# Тип num: <тип>, Тип text: <тип>, Тип is_active: <тип>.
#
# (Используй функцию type())..

num = 5
text = "Python"
is_active = True
print("Тип num:", type(num))
print("Тип text:", type(text))
print("Тип is_active:", type(is_active))

#Задача 3 (Преобразование типов данных)
#Даны переменные:
#num_str = "123"
#flag = "True"
#Напиши код, который:

#Преобразует num_str в целое число.

#Преобразует flag в булево значение.

#Выводит результаты и их типы после преобразования в формате:
#Число: <значение>, тип: <тип>
#Флаг: <значение>, тип: <тип>

#Подсказка: Используй int(), bool().

num_str = "123"
flag = "True"

num_int = int(num_str)
flag_bool = bool(flag)

print ("Число:", num_int, "тип:", type(num_int))
print ("Флаг:", flag_bool,  "тип:", type(flag_bool))

#Задача 4 (Операции сравнения)
#Даны переменные:
#x = 10
#y = 5
#Напиши код, который выводит результаты сравнения в формате:
#x > y: <результат>, x == y: <результат>, x <= y: <результат>.

x = 10
y = 5

print ("x > y:", x > y)
print ("x == y:" , x == y)
print ("x <= y:", x <= y)

#Задача 5 (Преобразование типов)
#Даны переменные:
num_str = "10"
num_float = 5.7
#Преобразуй num_str в целое число, а num_float — в строку,
# затем выведи их новые типы в том же формате, что и в задаче 2.

#Пример вывода:
#"Тип num_str после преобразования: <тип>".

num_str = "10"
num_float = 5.7

num_int = int(num_str)
num_string = str(num_float)

print("Тип num_str после преобразования:", type(num_int))
print("Тип num_float после преобразования:", type(num_string))

#Задача 4 (Операции сравнения)
#Даны переменные:
x = 7
y = 10
#Выведи результаты сравнения (>, <, ==, !=) в формате:
#"x > y: <результат>", "x == y: <результат>" и т.д.

x = 7
y = 10
print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)

# Задача 5 (Именование переменных)
# Напиши код, где:
# Объявлены две корректные переменные по PEP 8 (например, user_age).
# Объявлена некорректная переменная (например, 1name).
# Выведены их значения.
# Поясни в комментариях (#), почему третья переменная некорректна.

#Корректные переменные
name = "Артем"
age = 39

#Некорректная переменная, начинается с цифры
#Вызовет SyntaxError: invalid decimal literal
#2name = "Усман"

print(name)
print(age)

#Задача 6 (Переопределение переменной)
#Объяви переменную count = 5, затем:
#Переопредели её значение на 10
#Выведи новое значение
#Объясни в комментарии, что произошло

count = 5
# Переменная count теперь хранит 10 вместо 5
count = 10
print(count)

#Задача 7 (Классификация типов данных)
#Определи и выведи тип данных для каждого значения:
#3.14, "Hello", True, [1, 2, 3]
#Формат вывода:
#"Тип 3.14: <тип>" (и так для каждого).

num_float = 3.14
num_str = "Hello"
num_bool = True
num_list = [1, 2, 3]
print("Тип 3.14:", type(num_float))
print("Тип Hello:", type(num_str))
print("Тип True:", type(num_bool))
print("Тип [1, 2, 3]:", type(num_list))

#Задача 8 (Закрепление всего пройденного)

#Напиши код, где:
#Объявляются две переменные разных типов (число и строка)
#Выполняется арифметическая операция с их преобразованием (например, сложение числа с строкой через int())
#Проверяется тип результата
#Выводится пояснение в формате:
#"Результат: <значение>, тип: <тип>"

height = "189"
age = 39
result = int(height) + age
print(f"Результат: {result}, тип: {type(result)}")

#Задача 9 (Арифметические операции + преобразование типов)
#Дано:
price = "15.5"  # строка
tax = 2          # целое число
#Вычисли итоговую стоимость (price + tax) и выведи результат с типом в формате:
#"Итог: <значение>, тип: <тип>".

price = "15.5"
tax = 2

price_float = float(price)
sum_price_tax = price_float + tax

print(f"Итог: {sum_price_tax}, тип: {type(sum_price_tax)}")

#Задача 10 (Сравнение строк и чисел)
#Дано:

num_str = "100"
num_int = 100
#Сравни их через == и выведи результат в формате:
#"Строка и число равны? <ответ>".

num_str = "100"
num_int = 100
comparison =  num_str == num_int
print(f"Строка и число равны? {comparison}")

#Задача 11 (Список и типы)
#Дано:

my_list = [10, "текст", 3.14, False]
#Выведи тип каждого элемента в формате:
#"Элемент <значение>: <тип>"

my_list = [10, "текст", 3.14, False]

for element in my_list:
    print(f"Элемент {element}: {type(element)}")

#Задача 1:
#Дан список numbers = [1, 2, 3, 4, 5]. Выведи каждый элемент, умноженный на 2.

numbers = [1, 2, 3, 4, 5]

for element in numbers:
    print(element * 2)

count = 5
while count >= 1:
    print(count)
    count -= 1

#Условие:
#Дан список mixed = [10, "яблоко", 3.14, True].
#Выведи только числа (int и float) из этого списка.

mixed = [10, "яблоко", 3.14, True]

for element in mixed:
    if isinstance(element, (int, float)):
       print(element)

#Дан список:

data = [1, "кошка", 2.5, False, 100, "собака", 3.14]

for text in data:
   if isinstance(text, str):
       print(text)


#Задача 1 (Арифметические операции)
#Напиши код, который вычисляет сумму, разность, произведение и частное двух переменных a = 10 и b = 2.
#Выведи каждый результат в формате:
#"Сумма: {результат}" (и аналогично для остальных операций).

#Примечание: Учитывай, что деление может быть нецелым.

a = 10
b = 2

summa = a + b
difference = a - b
multiplication = a * b
division = a / b

print(f"Сумма: {summa}")
print(f"Разность: {difference}")
print(f"Произведение: {multiplication}")
print(f"Частное: {division}")

#Задача 2 (Типы данных и преобразование)
#Даны две переменные:


#num_str = "15"
#num_int = 3
#Напиши код, который:

#Преобразует num_str в целое число.

#Складывает преобразованное число с num_int.

#Выводит результат в виде:
#"Результат: {сумма}".

num_str = "15"
num_int = 3

result_int = int(num_str)

print(f"Результат: {num_int + result_int}")

#Задача 3 (Операции сравнения)
#Даны две переменные:

x = 7
y = 11
#Напиши код, который выводит результаты следующих сравнений:

#x больше y

#x не равно y

#y меньше или равно x + 5

x = 7
y = 11

print(f"1. {x > y}")
print(f"2. {x != y}")
print(f"3. {y <= x + 5}")


"""Задача 4 (Именование переменных)
Исправь некорректные имена переменных, соблюдая правила Python:

python
1user = "Anna"    # Ошибка: число в начале имени
User-Age = 25     # Ошибка: дефис в имени
print = 42        # Ошибка: имя встроенной функции
Что нужно сделать:

Переименуй переменные по правилам:

Без чисел в начале,

Без спецсимволов (кроме _),

Без конфликта с ключевыми словами.

Выведи их значения в формате:
{новое_имя}: {значение}.

Пример корректного имени: user_age."""

user_name = "Anna"
user_age = 25
user_id = 42

print(f"user_name: {user_name}")
print(f"user_age: {user_age}")
print(f"user_id: {user_id}")

"""Задача 5 (Переопределение переменной)
Дана переменная:

value = 10
Выведи её текущее значение.

Переопредели её, увеличив на 5.

Выведи новое значение в формате:
"Новое значение: {value}"""

value = 10
print(f"Текущее значение: {value}")

value_new = value + 5
print(f"Новое значение: {value_new}")

"""Задача 1 (Типы данных)
Напиши код, который создаёт три переменные:

num — целое число 10,

text — строку "Python",

flag — булево значение True.

Выведи их типы с помощью функции type()."""

num = 10
text = "Python"
flag = True

print(type(num))
print(type(text))
print(type(flag))

"""Задача 2 (Арифметические операции)
Даны две переменные:

python
a = 15
b = 4
Выведи результат сложения (+), вычитания (-), умножения (*), деления (/) и целочисленного деления (//) этих чисел.

Ответ должен содержать только код, без пояснений"""

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)

"""Задача 3 (Операции сравнения)
Даны две переменные:

python
x = 20
y = 35
Выведи результаты следующих сравнений:

x больше y,

x меньше или равно y,

x не равно y"""

x = 20
y = 35

print(x > y)
print(x <= y)
print(x != y)

"""Задача 4 (Преобразование типов данных)
Даны:

python
number_str = "123"
float_str = "45.67"
Преобразуй number_str в целое число, а float_str — в число с плавающей точкой, затем выведи их сумму.

Ответ должен содержать только код, без пояснений."""

number_str = "123"
float_str = "45.67"

number_int = int(number_str)
float_float = float(float_str)
print(number_int + float_float)

"""Задача 5 (Именование переменных)
Напиши код, где создаются три переменные по правилам именования в Python:

Переменная для хранения возраста (выбери осмысленное имя),

Переменная для хранения названия города (латиницей, без пробелов),

Переменная-константа для хранения числа Пи (3.14).

Ответ должен содержать только код, без пояснений."""

age = 39
city = "Kazan"
PI = 3.14

"""Задача 6 (Переопределение переменной)
Дана переменная:

python
value = 100
Выведи её текущее значение.

Переопредели её, увеличив на 50.

Выведи новое значение."""

value = 100
print(value)

value = 150
print(value)

"""Задача 7 (Классификация по типам данных)
Дан список:

python
data = [42, "Hello", 3.14, False, [1, 2]]
Напиши код, который выводит тип каждого элемента списка в формате:

text
<элемент> — <тип>
Ответ должен содержать только код, без пояснений."""

data = [42, "Hello", 3.14, False, [1, 2]]
for item in data:
    print(item, "—", type(item))

"""Задача 8 (Объявление переменных)
Создай 4 переменные:

name (строка с твоим именем),

age (целое число с твоим возрастом),

height (дробное число — рост в метрах, например 1.75),

is_student (булево значение — является ли студентом)."""

name = "Artem"
age = 39
height = 1.86
is_student = False

"""Задача 9 (Преобразование типов данных)
Даны:

python
num1 = "50"
num2 = 10
Сложи их так, чтобы получить целое число 60, и выведи результат.

Ответ должен содержать только код, без пояснений."""

num1 = "50"
num2 = 10
print(int(num1) + num2)

"""Задача 10 (Арифметические операции)
Даны:

python
x = 12
y = 5
Выведи остаток от деления x на y и результат возведения x в степень y"""

x = 12
y = 5

print(x % y)
print(x ** y)