#Задача 1 (Создание класса)
#Создай класс Dog без атрибутов и методов.

class Dog:
    ...

#Задача 2 (Конструктор класса __init__)
#Создай класс Student с конструктором __init__,
#который принимает два параметра: name (строка) и age (число). Присвой эти значения атрибутам объекта.

class Student:

    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

#Задача 3 (Методы класса)
#Добавь в класс Student метод introduce, который выводит строку:
#"Меня зовут {name}, мне {age} лет."

class Student:

    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")


student = Student("Мария", 19)
student.introduce()

#Задача 4 (Общие атрибуты)
#Добавь в класс Student общий атрибут school = "ИТМО" (доступный всем объектам).
#После этого создай два объекта и проверь, что они выводят одно и то же значение school.


class Student:
    school = "ИТМО"

    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет, я учусь в {self.school}.")

student = Student("Totti", 19)
student.introduce()

#Задача 5 (Методы и self)
#Добавь в класс Student метод have_birthday, который:
#Увеличивает возраст студента на 1.
#Выводит сообщение: «Теперь мне {новый возраст} лет!».

class Student:
    school = "ИТМО"

    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет, я учусь в {self.school}.")

    def have_birthday(self):
        self.age += 1
        print(f"Теперь мне {self.age} лет!")


student = Student("Totti", 19)
student.introduce()
student.have_birthday()

#Задача 6 (Работа с объектами)
#Создай класс Book с:
#Конструктором, принимающим title (название) и author (автор)
#Методом info(), который возвращает строку: "Книга: {title}, Автор: {author}"

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")



book = Book("Война и мир", "Толстой")
book.info()

#Задача 7 (Работа с несколькими объектами)
#Создай класс Rectangle с:
#Атрибутами width и height (задаются в конструкторе)
#Методом area(), который возвращает площадь прямоугольника
#Методом perimeter(), который возвращает периметр

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


result = Rectangle(5, 5)
result.area()
result.perimeter()

#Задача 8 (Параметр self)
#Создай класс Counter с:
#Атрибутом count (начальное значение 0)
#Методом increment(), который увеличивает count на 1
#Методом show(), который возвращает текущее значение count

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def show(self):
        return self.count


counter = Counter()
print(counter.show())
counter.increment()
print(counter.show())

#Задача 9 (Работа с несколькими объектами)
#Создай класс BankAccount с:
#Атрибутом balance (начальный баланс = 0)
#Методом deposit(amount) - пополняет баланс
#Методом withdraw(amount) - снимает деньги (если хватает средств)
#Методом check_balance() - возвращает текущий баланс

class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете!")

    def check_balance(self):
        return self.balance


account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.check_balance())

#Задача 10 (Комбинированная)
#Создай класс Calculator с:
#Атрибутом memory (хранит последний результат)
#Методами:
#add(a, b) — складывает числа, сохраняет результат в memory
#subtract(a, b) — вычитает, сохраняет результат
#get_memory() — возвращает значение memory

class Calculator:

    def __init__(self):
        self.memory = 0

    def add(self, a, b):
        self.memory += a + b

    def subtract(self, a, b):
        self.memory += a - b

    def get_memory(self):
        return self.memory

calculator = Calculator()
calculator.add(4, 8)
print(calculator.get_memory())
calculator.subtract(4, 3)
print(calculator.get_memory())
calculator.get_memory()

#Задача 11 (Базовый класс)
#Создай класс Animal:
#С атрибутом name (передаётся в __init__)
#С методом speak(), который возвращает "Я не знаю, какой звук издаю!"

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Я не знаю, какой звук издаю!"

animal = Animal("Мурзилка")
animal.speak()

#Задача 12 (Наследование)
#Расширь класс Animal, создав класс Dog:
#Переопредели метод speak(), чтобы возвращал "Гав!"
#Добавь метод fetch(item), который возвращает f"Принёс {item}!"


class Animal:  # Из задачи 11

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Я не знаю, какой звук издаю!"

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Гав!"

    def fetch(self, item):
        return f"Принёс {item}!"

dog = Dog("Бобик")
print(dog.name)
print(dog.speak())
print(dog.fetch("палку"))

#Задача 13 (Инкапсуляция)
#Создай класс BankAccount с:
#Пpиватным атрибутом __balance (начинается с 0)
#Методами:
#deposit(amount) — пополняет баланс
#withdraw(amount) — снимает деньги (если хватает)
#get_balance() — возвращает баланс

class BankAccount:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Недостаточно средств!")

    def get_balance(self):
        return self.__balance

bank = BankAccount()
bank.deposit(350)
print(bank.get_balance())
bank.withdraw(125)
print(bank.get_balance())

#Задача 14 (Полиморфизм)
#Создай классы Cat и Bird, наследующие от Animal:
#Cat.speak() → "Мяу!"
#Bird.speak() → "Чирик!"

class Animal:  # Из задачи 11

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Я не знаю, какой звук издаю!"

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Гав!"

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Мяу!"

class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Чирик!"

cat = Cat("Мурка")
print(cat.name)
print(cat.speak())

#Задача 15 (Магические методы)
#Добавь в класс Dog:
#__str__ → "Собака по имени {name}"
#__len__ → возвращает длину имени собаки

class Animal:  # Из задачи 11

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Я не знаю, какой звук издаю!"

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Собака по имени {self.name}"

    def fetch(self, item):
        return f"Принёс {item}!"


dog = Dog("Бобик")
print(dog.name)
print(dog.speak())
print(len(dog.name))

#Задача 1 (Создание класса)
#Создай класс Book, который будет представлять книгу.
#У класса должен быть один атрибут title (название книги), задаваемый при создании объекта.

class Book:

    def __init__(self, title):
        self.title = title


my_book = Book("Война и мир")
print(my_book.title)

#Задача 2 (Методы класса)
#Дополни класс Book из предыдущей задачи методом get_title,
#который возвращает название книги в верхнем регистре (заглавными буквами).

class Book:

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title.upper()

my_book = Book("Мастер и Маргарита")
print(my_book.get_title())

#Задача 3 (Параметр self)
#Создай класс Calculator с методом add, который принимает два числа и возвращает их сумму.
#Метод должен использовать параметр self, даже если он не задействован в вычислениях (для понимания синтаксиса).
#Добавь метод multiply для умножения! (По желанию.)

class Calculator:

    def add (self, a, b):
       return a + b

    def multiply (self, a, b):
        return a * b


calc = Calculator()
print(calc.add(3, 5))
print(calc.multiply(10, 26))


#Задача 4 (Общие атрибуты класса)
#Создай класс SpaceShip с:
#Общим для всех кораблей атрибутом fuel_type = "антиматерия" (задается на уровне класса).
#Атрибутом объекта name (задается при создании корабля).

class SpaceShip:
    fuel_type = "антиматерия"

    def __init__(self, name):
        self.name = name


ship1 = SpaceShip("Звездный разрушитель")
print(ship1.name)
print(ship1.fuel_type)

ship2 = SpaceShip("Серенити")
print(ship2.name)
print(ship2.fuel_type)

#Задача 5 (Класс + методы + self)
#Создай класс Robot с:
#Атрибутом объекта name (задается при создании).
#Методом greet(), который возвращает строку:
#"Я робот по имени {name}. Готов к работе!" (используй self).

class Robot:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Я робот по имени {self.name}. Готов к работе!"

    def upgrade(self):
        self.name = f"{self.name} v2.0"

r2d2 = Robot("R2-D2")
print(r2d2.greet())
r2d2.upgrade()
print(r2d2.name)

#Задача 6 (Конструктор + методы)
#Создай класс BankAccount:
#В конструкторе (__init__) задавай атрибуты:
#owner (владелец счета, строка)
#balance (баланс, число, по умолчанию 0)
#Добавь метод deposit(amount), который увеличивает balance на amount.
#Добавь метод withdraw(amount), который уменьшает balance на amount,
#но не позволяет уйти в минус (если средств нет, выводи "Недостаточно средств!").

class BankAccount:
    INTEREST_RATE = 0.01
    balance = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Начисляем проценты на текущий баланс
        interest = self.balance * self.INTEREST_RATE
        self.balance += interest
        # Добавляем новую сумму
        self.balance += amount
        print(f"Начислены проценты: {interest:.2f}₽")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств!")

    def display_balance(self): #Добавили метод display_balance() для красивого вывода информации
        return f"Ваш баланс {self.balance} рублей"



acc = BankAccount("Мария", 1000)
acc.deposit(500)
# Начислены проценты: 10.00₽ (1% от 1000)
# Баланс станет: 1000 + 10 + 500 = 1510₽
print(acc.display_balance())


#Задача 7 (Приватные атрибуты)
#Создай класс TemperatureSensor:
#Приватный атрибут __temperature (изначально 0).
#Публичный метод get_temperature(), который возвращает значение __temperature.
#Публичный метод set_temperature(value), который:
#Запрещает установку температуры ниже -273.15°C (абсолютный ноль),
#Выводит "Некорректное значение!" при попытке нарушить это правило.

class TemperatureSensor:
    __temperature = 0

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, value):
        if value < -273.15:
            print(f"Некорректное значение!")
        else:
            self.__temperature = value

sensor = TemperatureSensor()
sensor.set_temperature(25)
print(sensor.get_temperature())  # 25
sensor.set_temperature(-300)