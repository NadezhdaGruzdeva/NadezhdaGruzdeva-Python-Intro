# 22. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def SumEl(yourList):
    if len(yourList) < 2:
        return print('The list is to short')
    sumEl = 0
    for i in range(1, len(yourList), 2):
        sumEl += (yourList[i])
    return sumEl 


# myList = [2] 
myList = [2, 3, 5, 9, 3] 
print(f'Cумма элементов списка, стоящих на нечётной позиции = {SumEl(myList)}')