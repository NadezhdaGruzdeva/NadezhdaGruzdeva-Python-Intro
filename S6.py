# 42. Есть список чисел. Вывести – является ли последовательность строго убывающей, 
# или строго возрастающей, или ни то, ни другое

# my_list = [5, 1, 0, -2, -4]
# counterVozr = 0
# counterUbiv = 0
# for i in range(len(my_list)- 1):
#     if my_list[i] <  my_list[i + 1]:
#         counterVozr += 1
#     elif my_list[i] >  my_list[i + 1]:
#         counterUbiv += 1
#     else:
#         print("Последовательность не является ни строго возврастающей, ни строго убывающей")
#         break
# if counterUbiv == len(my_list)- 1:
#     print("Последовательность является строго убывающей")
# elif counterVozr == len(my_list)- 1:
#     print("Последовательность является строго возврастающей")

# 2 вариант
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

# print(s_dict[check_sorted([1, 2, 3])])
# print(s_dict[check_sorted([3, 2, 3])])
# print(s_dict[check_sorted([3, 2, 1])])
# print(check_sorted([1, 1, 2, 3]))

# 2. Дана последовательность чисел. Получить отсортированный по возрастанию список 
# уникальных элементов заданной последовательности.
# 	Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [100, 2, 3, 5, 1, 5, 3, 10]
# unique_list = [i for i in my_list if my_list.count(i) == 1]
# print(sorted(unique_list))

# Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 
# (9 элементов). Двумерный массив заполнен числами от 1 до 9.
# Функция должна вернуть False, если в массиве все числа от 1 до 9 
# встречаются ровно один раз. В противном случае True.
# [[1, 3, 2], [9, 7, 8], [4, 5, 6]] ➞ False
# [[8, 9, 2], [5, 6, 1], [3, 7, 4]] ➞ False
# [[1, 1, 3], [6, 5, 4], [8, 7, 9]] ➞ True # 1 дублируется
# [[1, 2, 3], [3, 4, 5], [9, 8, 7]] ➞ True # 3 дублируется

# matrix = [[1, 3, 2], [9, 9, 8], [4, 5, 6]]
# matrix1 = [item for j in matrix for item in j]
# print(sorted(matrix1) != [1,2,3,4,5,6,7,8,9])
# def any_duplicates(matr):
#     perfect_array = [1,2,3,4,5,6,7,8,9]
#     array = []
#     for i in matr:
#         for j in i:
#             array.append(j)
#     sorted_array = sorted(array)
#     return sorted_array != perfect_array
# print(any_duplicates(matrix))

Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.
	Пример:
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
**Добавьте возможность использования скобок, меняющих приоритет операций.
	Пример:
1+2*3 => 7;
(1+2)*3 => 9;
