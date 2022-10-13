# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

def SpecDict():
    n = int(input('Enter the number \n'))
    dictForSequence = {}
    for i in range (1, n + 1):
        dictForSequence[i] = round((1 + 1 / i) ** i, 2)
    print(dictForSequence)
SpecDict()