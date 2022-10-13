# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

def CreateListFromNegatToPositive(N):
    myList = []
    indexForMyList = 0
    if N > 0:
        for i in range (-N, N + 1):
            myList.append(i)
            indexForMyList += 1
    else:
        for i in range(-N, N - 1, -1):
            myList.append(i)
            indexForMyList -= 1
    return(myList)   

n = int(input('Enter the number \n'))
myList = CreateListFromNegatToPositive(n)
print(myList)
index1 = int(input('Enter first position of value for muliplication (start from 1) \n'))
index2 = int(input('Enter second position of value for muliplication (start from 1) \n'))
multiplic = myList[index1 - 1] * myList[index2 - 1]
print(f'Result of multiplication of values {myList[index1 - 1]} and {myList[index2 - 1]} is {multiplic}')
