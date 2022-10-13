# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def MultiplFibanachi():
    N = int(input('Enter the number \n'))
    multiplList = []
    valueMultiplList = 1
    if N > 0:
        for i in range (N):
            valueMultiplList *= (i + 1)
            multiplList.append(valueMultiplList)
    
    else:
        for i in range(1, N - 1, -1):
            multiplList.append(valueMultiplList)
            valueMultiplList *= (i - 1)
    print(multiplList)   

MultiplFibanachi()