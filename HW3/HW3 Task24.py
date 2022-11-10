# 24. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from turtle import left


def FractDifference(yourList):
    leftovers = []
    for i in range(len(yourList)):
        leftover = abs(yourList[i]) % 1 #abs for negative values
        if leftover > 0:
            leftovers.append(leftover)
    print(leftovers)
    return round(max(leftovers) - min(leftovers),2)

myList = [1.1, 1.2, 3.1, 5, -10.01]
print (f'Разница = {FractDifference(myList)} ')
