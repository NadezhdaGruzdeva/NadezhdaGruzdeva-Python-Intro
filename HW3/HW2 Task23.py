# 23. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def MultPairVal(yourList):
    import math
    lenYourList = len(yourList)
    multList =[]
    for i in range(math.ceil(lenYourList/2)):
        multList.append(yourList[i] * yourList[lenYourList - 1 - i])
    return multList

myList = [2, 3, 4, 5, 6]
# myList = [2, 3, 5, 6]
print(MultPairVal(myList))
