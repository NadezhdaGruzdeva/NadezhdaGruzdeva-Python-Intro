# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def SumFiguresOfRealEnteredNumber ():
    number = float(input('Enter the real number \n'))
    numberStr = str(number)
    figuresOnlyStr = numberStr.replace('.','')
    figuresOnlyStr = figuresOnlyStr.replace('-','')
    figuresQty = len(figuresOnlyStr)
    figuresSum = 0
    for i in range(figuresQty):
        figuresSum += int(figuresOnlyStr[i])
    print(f'Figures sum of entered number = {figuresSum}')

SumFiguresOfRealEnteredNumber()
