# 32. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

#Классный ввод списка через map
my_list = list(map(int, input("Enter the list of numbers devided by space: ").split())) 
# n = int(input('Введите количество чисел в последователности '))
# my_list = []
# for i in range(n):
#     value = my_list.append(int(input('Введите число ')))

print(f'Entered list: {my_list}')

list_unuque = list(filter(lambda x: my_list.count(x) == 1, my_list)) #lambda and filter
# for i in my_list:
#     if my_list.count(i) == 1:
#         list_unuque.append(i)

print(f'List of unique values: {list_unuque}')

