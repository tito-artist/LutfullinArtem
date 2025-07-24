#Задача 1 (Создание словаря)
#Создай словарь fruit_prices, где ключами будут названия фруктов ('яблоко', 'банан', 'апельсин'),
# а значениями — их цены в рублях (50, 30, 70 соответственно). Выведи словарь на экран.
#Примечание: Задачи будут идти в случайном порядке из всех разделов темы.

fruit_prices = {
    "яблоко": 50,
    "банан": 30,
    "апельсин": 70
}
print(fruit_prices)

#Задача 2 (Доступ к элементам словаря по ключу)
#Дан словарь:

"""student = {
    "имя": "Алексей",
    "возраст": 20,
    "курс": 2
}"""
#Выведи на экран возраст студента, используя ключ словаря.

#Дополнительное задание (если хочешь усложнить):
#Попробуй также получить значение по ключу "группа",
#но обработай ситуацию, если такого ключа нет, чтобы программа не падала с ошибкой (выведи "Ключ не найден").

student = {
    "имя": "Алексей",
    "возраст": 20,
    "курс": 2
}
result = student["возраст"]
print(result)
print(student.get("группа", "Ключ не найден"))

#Задача 3 (Добавление и обновление элементов словаря)
#Дан словарь:

"""car = {
    "марка": "Toyota",
    "модель": "Camry",
    "год": 2020
}"""
#Добавь в него новый ключ "цвет" со значением "синий".

#Обнови значение ключа "год" на 2022.

#Выведи итоговый словарь на экран.

car = {
    "марка": "Toyota",
    "модель": "Camry",
    "год": 2020
}

car["цвет"] = "синий"
car["год"] = 2022

print(car)

#Задача 4 (Удаление элементов словаря)
#Дан словарь:

"""book = {
    "название": "1984",
    "автор": "Джордж Оруэлл",
    "год": 1949,
    "жанр": "антиутопия"
}"""
#Удали ключ "год" с помощью оператора del.

#Удали ключ "жанр" с помощью метода .pop() и сохрани значение в переменную deleted_genre.

#Выведи итоговый словарь и отдельно переменную deleted_genre.

book = {
    "название": "1984",
    "автор": "Джордж Оруэлл",
    "год": 1949,
    "жанр": "антиутопия"
}

del book["год"]
deleted_genre = book.pop("жанр")

print(book)
print(deleted_genre)

#Задача 5 (Методы keys(), values(), items())
#Дан словарь:

"""country = {
    "название": "Япония",
    "столица": "Токио",
    "население": 125_800_000,
    "язык": "японский"
}"""
#Выведи все ключи словаря в виде списка.

#Выведи все значения словаря в виде списка.

#Выведи все пары "ключ-значение" в виде списка кортежей.

country = {
    "название": "Япония",
    "столица": "Токио",
    "население": 125_800_000,
    "язык": "японский"
}
keys = country.keys()
values = country.values()
elements = country.items()

print(list(keys))
print(list(values))
print(list(elements))

#Задача 6 (Проверка элементов)
#Дан словарь:

"""smartphone = {
    "модель": "Galaxy S23",
    "бренд": "Samsung", 
    "год выпуска": 2023,
    "цвет": "чёрный"
}"""
#Проверь, есть ли в словаре ключ "цена" (выведи True или False).

#Проверь, есть ли среди значений словаря число 2023 (выведи True или False).

#Дополнительно: Проверь наличие пары "бренд": "Samsung" через метод .items().

smartphone = {
    "модель": "Galaxy S23",
    "бренд": "Samsung",
    "год выпуска": 2023,
    "цвет": "чёрный"
}
print("цена" in smartphone)  # Проверка ключа
print(2023 in smartphone.values())  # Проверка значения
print(("бренд", "Samsung") in smartphone.items())  # Проверка пары

#Задача 7 (Комбинированная)
#Дан словарь:

"""movie = {
    "title": "Inception",
    "year": 2010,
    "director": "Christopher Nolan",
    "genre": "sci-fi"
}"""
#Добавь новый ключ "rating" со значением 8.8.

#Проверь, есть ли в словаре ключ "budget" (выведи True/False).

#Удали ключ "genre" методом .pop(), сохрани значение в переменную deleted_genre.

#Выведи:

#Итоговый словарь

#Удалённое значение deleted_genre

#Список всех оставшихся ключей

movie = {
    "title": "Inception",
    "year": 2010,
    "director": "Christopher Nolan",
    "genre": "sci-fi"
}

movie["rating"] = 8.8 #Добавляем новый ключ "rating" со значением 8.8
print("budget" in movie) #Проверяем, есть ли в словаре ключ "budget" (выводим True/False)
deleted_genre = movie.pop("genre") #Удаляем ключ "genre" методом .pop() и сохраняем значение в переменную deleted_genre

print(movie)  #Итоговый словарь
print(deleted_genre) #Удалённое значение deleted_genre
print(list(movie.keys())) #Список всех оставшихся ключей

#Задача 8 (Вложенные словари и комплексные операции)
#Дан словарь фильмов:

"""movies = {
    "Inception": {
        "year": 2010,
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        "rating": 8.8
    },
    "The Matrix": {
        "year": 1999,
        "director": "Lana Wachowski",
        "actors": ["Keanu Reeves", "Laurence Fishburne"],
        "rating": 8.7
    }
}"""
#Задания:

#Добавь новый фильм "Interstellar" (год: 2014, режиссёр: Nolan, актёры: ["McConaughey", "Hathaway"], рейтинг: 8.6).

#Обнови список актёров в "The Matrix", добавив "Carrie-Anne Moss".

#Проверь, есть ли фильм с рейтингом выше 8.8 (выведи True/False).

#Выведи всех режиссёров (без повторений) в формате: Режиссёры: Nolan, Lana Wachowski.

movies = {
    "Inception": {
        "year": 2010,
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        "rating": 8.8
    },
    "The Matrix": {
        "year": 1999,
        "director": "Lana Wachowski",
        "actors": ["Keanu Reeves", "Laurence Fishburne"],
        "rating": 8.7
    }
}

#Добавление нового фильм "Interstellar"

movies["Interstellar"] = {
    "year": 2014,
    "director": "Christopher Nolan",
    "actors": ["McConaughey", "Hathaway"],
    "rating": 8.6
}

#Обновление списка актёров в "The Matrix"

movies["The Matrix"]["actors"] = ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]

#Проверка, есть ли фильм с рейтингом выше 8.8 (выведи True/False)

print("rating" > 8.8 in movies.values())
print(movies.values("director"))