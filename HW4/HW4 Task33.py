# 33. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в 
# файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

from random import randint

k = int(input('Задайте натуральную степень '))
# k = 10
ratiosList = []
for i in range(k + 1):
    ratiosList.append(randint(1, 100))
print(f'Список коэффициентов: {ratiosList}') 
formula = ''
for i in range(k-1):
    formula = formula + str(ratiosList[i]) + 'x' + '^' + str(k - i) + ' + '
formula = formula + str(ratiosList[k-1]) + 'x' + ' + '
formula = formula + str(ratiosList[k]) + ' = 0'

print(formula)
# print(type(formula))

with open('Task33 Polnominal.txt', 'w') as p:
    p.write(formula)
