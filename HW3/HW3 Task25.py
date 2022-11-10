# 25. Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def ToBinary(number):
    strFig = ''
    while number > 1:
        strFig = str(abs(number) % 2) + strFig
        number = abs(number) // 2
    if number == 1:
        strFig = str(1) + strFig
    else:
        strFig = str(0) + strFig
    return strFig

n = int(input('Enter the number \n'))
print (f'Deciml number {n} = binary number {ToBinary(n)}.')

