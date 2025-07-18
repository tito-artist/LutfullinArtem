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
