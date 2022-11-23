'''
42. Есть список чисел. Вывести – является ли последовательность строго убывающей, или строго возрастающей, или ни то, ни другое
'''

# def check_sorted(my_list):
#     count = 0
#     for i in range(1, len(my_list)):
#         count += my_list[i] - my_list[i-1]
#     if count == len(my_list) - 1:
#         print('Возрастает')
#     elif count == -(len(my_list) - 1):
#         print('Убывает')
#     else:
#         print('Ни то, ни то')
#
# check_sorted([1, 2, 3, 4])
# check_sorted([4, 3, 2, 1])
# check_sorted([1, 2, 3, 2])
# check_sorted([1, 4, 3, 4]) # ломает

# def check_sorted(somelist):
#     if sorted(set(somelist)) == somelist:
#         return 1
#     elif sorted(set(somelist), reverse=True) == somelist:
#         return -1
#     return 0
# s_dict = {
#     1: 'Возрастает',
#     -1: 'Убывает',
#     0: 'Ни то, ни то'
#           }
#
# print(s_dict[check_sorted([1, 2, 3])])
# print(s_dict[check_sorted([3, 2, 3])])
# print(s_dict[check_sorted([3, 2, 1])])
# print(check_sorted([1, 1, 2, 3]))

"""
43. Дана последовательность чисел. Получить отсортированный по возрастанию
список уникальных элементов заданной последовательности.
*Пример:* 
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
"""

# import random
#
# my_list = [random.randint(1, 10) for i in range(10)]
# print(my_list)
# print(set(my_list))

# print(new_list)
#
# only_ones = []
# for el in new_list:
#     if my_list.count(el) == 1:
#         only_ones.append(el)
#
# print(only_ones)


#
# def sort_lst(lst: list) -> list:
#     uniq_elements = set()
#     for el in lst:
#         if el not in uniq_elements:
#             uniq_elements.add(el)
#         else:
#             uniq_elements.discard(el)
#
#     s = list(uniq_elements)
#     s.sort()
#     return s
#
# lst = [1, 2, 3, 5, 1, 5, 3, 10]
# print(sort_lst(lst))  # [2, 10]


'''
42. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
Пример:
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
Добавьте возможность использования скобок, меняющих приоритет операций.
Пример:
1+2*3 => 7;
(1+2)*3 => 9;
'''


string = '1+23*3-2*4'

def list_from_string(string:str):

    result = []
    temp = 0
    for i in range(0, len(string)):

        if not string[i].isalnum():
            result.append(string[temp:i])
            result.append(string[i])
            temp = i + 1

    result.append(string[temp:])
    print(result)

    return result

def simple_math(operation:list):
    if operation[1] == '/':
        return [str(float(operation[0]) / float(operation[2]))]
    if operation[1] == '*':
        return [str(float(operation[0]) * float(operation[2]))]
    if operation[1] == '+':
        return [str(float(operation[0]) + float(operation[2]))]
    if operation[1] == '-':
        return [str(float(operation[0]) - float(operation[2]))]

def do_math(equation:list):

    while len(equation) != 1:
        for sign in '/*+-':
            while sign in equation:
                idx = equation.index(sign)
                equation = equation[:idx-1] + simple_math(equation[idx-1:idx+2]) + equation[idx+2:]

    return equation

print(do_math(list_from_string(string)))


# my_str = input("Введите пример: ")
# my_list = []
# for i in my_str:
#     my_list.append(i)
# print(my_list)
# for j in range(2):
#     for i in range(len(my_list)):
#         if i < len(my_list):
#             if my_list[i] == '*':
#                 my_list[i] = int(my_list[i - 1]) * int(my_list[i + 1])
#                 my_list.pop(i - 1)
#                 my_list.pop(i)
#             elif my_list[i] == '/':
#                 my_list[i] = int(my_list[i - 1]) / int(my_list[i + 1])
#                 my_list.pop(i - 1)
#                 my_list.pop(i)
#         else:
#             break
# print(my_list)
# for j in range(2):
#     for i in range(len(my_list)):
#         if i < len(my_list):
#             if my_list[i] == '+':
#                 my_list[i] = int(my_list[i - 1]) + int(my_list[i + 1])
#                 my_list.pop(i - 1)
#                 my_list.pop(i)
#             elif my_list[i] == '-':
#                 my_list[i] = int(my_list[i - 1]) - int(my_list[i + 1])
#                 my_list.pop(i - 1)
#                 my_list.pop(i)
#         else:
#             break
# print(my_list)


# my_str = input('Введите выражение: ')
# my_list =list(filter(lambda x: x.isdigit(), my_str))
# sign = list(filter(lambda x: not x.isdigit(), my_str))
#
# print(sign)
#
# print(eval(my_str))
#


# import re
#
# actions = {
#     "^": lambda x, y: str(float(x) ** float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y))
# }
#
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
#
#
# def my_eval(expresion: str) -> str:
#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
#
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
#
#     return expresion
#
#
# exp = "(1 + 4) * (5 * (10 - 2)) / 5"
# print(my_eval(exp), eval(exp))  # 40.0 40.0

"""
45. Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов). Двумерный массив заполнен числами от 1 до 9.
Функция должна вернуть False, если в массиве все числа от 1 до 9 встречаются ровно один раз. В противном случае True.
[[1, 3, 2], [9, 7, 8], [4, 5, 6]] ➞ False
[[8, 9, 2], [5, 6, 1], [3, 7, 4]] ➞ False
[[1, 1, 3], [6, 5, 4], [8, 7, 9]] ➞ True # 1 дублируется
[[1, 2, 3], [3, 4, 5], [9, 8, 7]] ➞ True # 3 дублируется
"""


# def search_dubls(some_list):
#     new_list = [i for x in some_list for i in x]
#     return sorted(new_list) != [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# print(search_dubls([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))
