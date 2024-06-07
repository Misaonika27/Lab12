#НАЧАЛО Задания №6
def greet():
    print("Привет, мир!")
def print_name(name):
    print(name)
def calculate_discriminant(a, b, c):
    return b ** 2 - 4 * a * c
def ask_user_info():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    return name, age
def get_russian_alphabet_letter(number):
    if number <= 33:
        return chr(ord('а') + number - 1)
    else:
        print("Указано неправильное число!")

# Примеры использования функций:
greet()
print_name("Ваше имя")
print(calculate_discriminant(1, 7, 6))
user_name, user_age = ask_user_info()
print("Ваше имя:", user_name)
print("Ваш возраст:", user_age)
print(get_russian_alphabet_letter(5))
#КОНЕЦ Задания №6

#НАЧАЛО Задания №7
# Создаем строковую переменную с ФИО
full_name = "Субботина Екатерина Александровна"

# Печатаем длину строки
print("Длина строки:", len(full_name))

# Печатаем результат конкатенации
print("Результат конкатенации:", full_name)

# Печатаем только имя (первое слово)
print("Только имя:", full_name.split()[1])

# Печатаем ФИО в верхнем регистре
print("ФИО в верхнем регистре:", full_name.upper())

# Разбиваем строку по пробелу
name_parts = full_name.split()
print("Разбитое ФИО по пробелу:", name_parts)
#КОНЕЦ Задания №7

#НАЧАЛО Задания 8

# Создаем список из 7 элементов разных типов
my_list = [None, 5, 3.14, "hello", [1, 2, 3], (4, 5, 6), {"name": "John"}]

# Печатаем тип каждого элемента списка
for item in my_list:
    print(type(item))

# Удаляем последний элемент списка
my_list.pop()

# Создаем список из букв ФИО
full_name = "Субботина Екатерина Александровна"
letters_list = list(full_name)

# Создаем строковую переменную с ФИО
full_name_string = ''.join(letters_list)

# Печатаем порядковый номер и символы ФИО
for index, letter in enumerate(letters_list):
    print(f"Порядковый номер: {index}, Символ: {letter}")

# Печатаем количество символов 'а' в списке букв ФИО
print("Количество символов 'а':", letters_list.count('а'))
#КОНЕЦ Задания 8

#НАЧАЛО Задания 9
# Генератор списка нечетных чисел от 1 до 100
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]

# Выводим список
print(odd_numbers)
#КОНЕЦ Задания 9

#НАЧАЛО Задания 10
def safe_division(dividend, divisor):
    if divisor == 0:
        print("Ошибка: Деление на ноль невозможно!")
        return None
    else:
        return dividend / divisor

# Пример использования функции
result = safe_division(10, 2)
print("Результат деления:", result)

result = safe_division(5, 0)
#КОНЕЦ Задания 10