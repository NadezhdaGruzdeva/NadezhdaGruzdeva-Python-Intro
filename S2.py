# trian
# Выяснить, является ли число кратным заданному, если нет, вывести остаток
number = int(input ("Enter number for devision "))
devider = int(input ("Enter devider "))
leftover = number % devider
if leftover == 0:
    print (f"Entered number ({number}) is multiple of entered devider ({devider})")
else:
    print (f"Entered number ({number}) isn't multiple of entered devider ({devider}). Leftor is {leftover}")

# Показать последнюю цифру 3-значного числа
number = int(input ("Enter number for devision "))
figure3 = number % 10
print (f'Third figure of entered number ({number}) is {figure3}')

color = ['red', 'green', 'yellow']
print(type(colors))

color.appent #add element at the end of list 
position =color.index ('green')
color.remove('white') #delete firs matched element
item = color.index #delete last element

# Напишите программу, которая принимает на вход число N и выдаёт 
# последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81
number = int(input ("Enter "))
output = 1
list = []
for i in range(1, number+1):
    list.append(output)
    output *= -3
print(f'Для N = {number}: {list}')

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
number = int(input ("Enter "))
dictionary = {}
for i in range(1, number+1):
    dictionary [i] = 3 * i + 1
print(f'Для N = {number}: {dictionary}')

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

str1 = input ("Enter str1 ")
str2 = input ("Enter str2 ")

if len(str1) > len(str2):
    myCounter = str1.count(str2)
else:
    myCounter = str2.count(str1)
print (myCounter)

    









