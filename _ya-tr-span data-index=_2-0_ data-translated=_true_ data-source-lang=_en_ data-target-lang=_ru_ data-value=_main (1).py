#НАЧАЛО Задания 1
print("Привет, Мир!")
# КОНЕЦ Задания 1


#НАЧАЛО Задания 2
# Создание переменных различных типов
none_var = None
int_var = 10
float_var = 3.14
str_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3, 4, 5)
dict_var = {'a': 1, 'b': 2, 'c': 3}
set_var = {1, 2, 3, 4, 5}

# Печать типа каждой переменной
print(f"Тип переменной none_var: {type(none_var)}")
print(f"Тип переменной int_var: {type(int_var)}")
print(f"Тип переменной float_var: {type(float_var)}")
print(f"Тип переменной str_var: {type(str_var)}")
print(f"Тип переменной list_var: {type(list_var)}")
print(f"Тип переменной tuple_var: {type(tuple_var)}")
print(f"Тип переменной dict_var: {type(dict_var)}")
print(f"Тип переменной set_var: {type(set_var)}")

# Изменение типов int и float
int_var = float(int_var)
float_var = str(float_var)

# Печать размера для строк и коллекций
print(f"Размер строки str_var: {len(str_var)}")
print(f"Размер списка list_var: {len(list_var)}")
print(f"Размер кортежа tuple_var: {len(tuple_var)}")
print(f"Первый элемент строки str_var: {str_var[0]}")
print(f"Последний элемент строки str_var: {str_var[-1]}")
print(f"Элементы кроме первого и последнего в строке str_var: {str_var[1:-1]}")

# Печать значения одного из ключей для словаря
key = next(iter(dict_var))
print(f"Значение для ключа '{key}' в словаре dict_var: {dict_var[key]}")
# КОНЕЦ Задания 2


#НАЧАЛО Задания 3
# Создание переменных типа bool
bool_var1 = True
bool_var2 = False

# Печать типа каждой переменной
print("Тип переменной bool_var1:", type(bool_var1))
print("Тип переменной bool_var2:", type(bool_var2))

# Логические операции
print("Результат конъюнкции (and):", bool_var1 and bool_var2)
print("Результат дизъюнкции (or):", bool_var1 or bool_var2)
print("Результат инверсии (not) для bool_var1:", not bool_var1)
print("Результат инверсии (not) для bool_var2:", not bool_var2)

# Создание переменных типа int
int_var1 = 10
int_var2 = 5

# Операции сравнения
print("Равны ли две переменные:", int_var1 == int_var2)
print("Не равны ли две переменные:", int_var1 != int_var2)
print("Больше ли первая переменная второй:", int_var1 > int_var2)
print("Меньше ли первая переменная второй:", int_var1 < int_var2)
print("Больше или равно ли значение второй переменной относительно первой:", int_var2 >= int_var1)
print("Меньше или равно ли значение второй переменной относительно первой:", int_var2 <= int_var1)

# Арифметические операции
print("Результат сложения:", int_var1 + int_var2)
print("Результат вычитания:", int_var1 - int_var2)
print("Результат умножения:", int_var1 * int_var2)
print("Результат деления:", int_var1 / int_var2)
print("Результат возведения в степень:", int_var1 ** int_var2)
print("Результат деления по модулю:", int_var1 % int_var2)
print("Результат целочисленного деления:", int_var1 // int_var2)
# КОНЕЦ Задания 3

#НАЧАЛО Задания 4
# Запрос ввода числа у пользователя
number = int(input("Введите число на интервале [-100; 100]: "))

# Проверка введенного числа и вывод соответствующего сообщения
if number < -100 or number > 100:
    print("Число не входит в диапазон [-100; 100]")
elif number == -50:
    print("Число равно -50")
elif -50 < number < 0:
    print("Число меньше 0, но больше -50")
elif 0 < number < 50:
    print("Число больше 0, но меньше 50")
elif number == 50:
    print("Число равно 50")
elif number < -50:
    print("Число меньше -50")
else:
    print("Число больше 50")
# КОНЕЦ Задания 4


#НАЧАЛО Задания 5
# Цикл for для печати чисел от 0 до 10
print("Цикл for:")
for i in range(11):
    print(i, end=' ')
print("\n")

# Цикл while для печати чисел от 0 до 10
print("Цикл while:")
j = 0
while j <= 10:
    print(j, end=' ')
    j += 1
print("\n")

# Создание строковой переменной с ФИО
fio = "Субботина Екатерина Александровна"

# Цикл for для печати каждой буквы ФИО
print("Буквы в ФИО:")
for letter in fio:
    print(letter, end=' ')
print("\n")

# Создание списка с именами друзей
friends = ["Оля", "Никита", "Женя"]

# Цикл for для печати имен друзей
print("Имена друзей:")
for friend in friends:
    print(friend)

# Создание словаря с датами рождения друзей
birthdays = {
    "Оля": "28.12.2002",
    "Никита": "01.05.2001",
    "Женя": "29.08.1994"
}

# Цикл for для печати имен и дат рождения друзей, родившихся летом или зимой
print("Друзья, родившиеся летом или зимой:")
for friend, birthday in birthdays.items():
    month = int(birthday.split('.')[1])
    if month in [6, 7, 8, 12, 1, 2]:
        print(f"{friend}: {birthday}")
# КОНЕЦ Задания 5