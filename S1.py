a = int(input('Введите \nа: '))
b = int(input('Введите \nb: '))
c = a + b
print('{} + {} = {}'.format(a, b, c))

#Тренировка
# Вывести квадрат числа
a = int(input('Введите \nа: '))
b = a ** 2
# print('квардрат числа а (', a, ') = ', b)
print(f'квардрат числа а ({a}) = {b}')

# Даны 2 числа. Показать большее и меньшее.
a = int(input('Введите \nа: '))
b = int(input('Введите \nb: '))
if a > b :
    print(f'number a ({a}) highter then number b {b}')
else:
    print(f'number b ({b}) highter then number a {a}')

# Выяснить, является ли число четным
a = int(input('Введите \nа: '))
if a % 2 == 1 :
    print(f'number a ({a}) is odd number')
else:
    print(f'number a ({a}) is even number')

# Вывести все четные числа от 1 до N
a = int(input('Введите \nа: '))
for i in range(2, a + 1, 2):
    print(i)

# Task1 Напишите программу, которая принимает на вход два числа и 
# проверяет, является ли одно число квадратом другого.
# Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8, 9 -> нет
a = int(input('Введите \nа: '))
b = int(input('Введите \nb: '))
if a ** 2 == b or b ** 2 == a :
    print('одно из введенных чисел равно квадрату другого')
else:
    print('одно из введенных чисел не равен квадрату другого')

# TASK 2 Напишите программу, которая на вход принимает 5 чисел и 
# находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# a = int(input('Введите \nа: '))
numbers = [1, 1, -5, 9, 2]
max = numbers [0]
for i in numbers:
    if i > max:
        max = i
print (max)

# TASK 3 Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
a = int(input('Введите \nа: '))
for i in range(-a , a + 1):
    print(i)

# TASK 4 Напишите программу, которая будет принимать на вход 
# дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3
a = float(input('Введите \nа: '))
b = int (a * 10 % 10)
print (b)

# TASK 5 Напишите программу, которая принимает на вход число и 
# проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a = int(input('Введите \nа: '))
if (a % 5 == 0 or a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
    print  (f'число {a} кратно 5 и 10 или 15, но не 30')
else:
    print  (f'число {a} не соответствует заданному условию')


