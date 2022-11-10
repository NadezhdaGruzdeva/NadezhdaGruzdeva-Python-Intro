'''
27. Задайте строку из набора чисел. Запишите ее в файл. Напишите программу, которая считает строку 
из файла и покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
'''
# string = '12 -5 34 71 -74 39 0'
# with open('task_27.txt', 'w') as f:
#     f.write(string)
#
# with open('task_27.txt') as file:
#     my_str = file.read()
#
#
# def find_max_min(str_1):
#     my_list = [int(x) for x in str_1.split()]
#     return min(my_list), max(my_list)
#
#
# new_str = '12374 12 65 '
# a, b = find_max_min(my_str)
#
# print(a, b)
# print(f'Минимальный элемент {a}')

'''
28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
с помощью математических формул нахождения корней квадратного уравнения
с помощью дополнительных библиотек Python
При этом функцию для нахождения дискриминанта импортируйте из файла utils.py

'''

# from math import sqrt
# from utils import discr
#
#
# def coren(a, b, c):
#     if discr(a, b, c) < 0:
#         print('Корней нет')
#     elif discr(a, b, c) == 0:
#         return -b / 2 * a
#     else:
#         return [(-b - sqrt(discr(a, b, c))) / 2 * a, (-b + sqrt(discr(a, b, c))) / 2 * a]
#
#
# print(coren(-4, 2, 1))

# import math


# def find_roots(a, b, c):
#     D = b ^ 2 - 4 * a * c
#     roots = []
#     if D < 0:
#         roots.append('Нет корней')
#         return roots
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     roots.append(x1)
#     if D > 0:
#         x2 = (-b - math.sqrt(D)) / (2 * a)
#         roots.append(x2)
#     return roots
#
#
# a, b, c = 1, -2, 8
# print(find_roots(a, b, c))

# from utils import discr
#
# def find_roots(a, b, c):
#     D = discr(a, b, c)
#     roots = []
#     x1 = (-b + D ** 0.2) / (2 * a)
#     roots.append(x1)
#     x2 = (-b - D ** 0.5) / (2 * a)
#     roots.append(x2)
#     return set(roots)
#
# a, b, c = 4, 4, 15
# print(find_roots(a, b, c))


'''
29.
Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
Это наименьшее натуральное число, которое делится и на «а», и на «b». 
Например: у нас есть два целых числа 4 и 6. 
Найдем НОК: Кратные 4: 4, 8, 12, 16, 20, 24, 28, 32, 36,... 
Кратные 6: 6, 12, 18, 24, 30, 36, 42,...
Общие кратные 4 и 6 — это просто числа, которые есть в обоих списках: 12, 24, 36, 48, 60, 72,.... 
НОК — это наименьший общий множитель, поэтому он равен 12.

'''


# def calculate_lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         greater += 1
#     return lcm

# #
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# # #
# print(f'НОК чисел {num1} и {num2} равен {calculate_lcm(num1, num2)}')
#
# from math import lcm, gcd
#
# def get_lcm(a, b):
#     return lcm(a, b)
#
#
# print(f'НОК чисел {num1} и {num2} равен {get_lcm(num1, num2)}')
#
# print(f'НОД чисел {num1} и {num2} равен {gcd(num1, num2)}')


# import math

#
# help(math)


# A = 1
# B = -8
# C = 12
#
# from utils import discr as ds
# from  math import sqrt
# x1 = -B- sqrt(ds(A, B, C))/2*A
# x2 = -B + sqrt(ds(A, B, C))/2*A
#
# print(x1, x2)


'''
27. Задайте строку из набора чисел. Запишите ее в файл. 
Напишите программу, которая считает строку из файла и покажет 
большее и меньшее число. В качестве символа-разделителя используйте пробел.
'''
# def find_max_min(str_1):
#     my_list = [int(x) for x in str_1.split()]
#     return min(my_list), max(my_list)

# my_string = '1 2 4 0 -3' 
# with open('s4.txt', 'w') as s4:
#     s4.write(my_string)
# with open('s4.txt', 'r') as s4:
#     readedString = s4.read()
# l1 = readedString.split(' ')
# print(readedString)
# print(type(readedString))
# print(l1)
# print(type(l1))
# my_list = []
# for el in l1:
#     my_list.append(int(el))
# print(my_list)
# print(type(my_list))
# print(max(my_list), min(my_list))

'''
28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
с помощью математических формул нахождения корней квадратного уравнения
с помощью дополнительных библиотек Python
При этом функцию для нахождения дискриминанта импортируйте из файла utils.py

'''


