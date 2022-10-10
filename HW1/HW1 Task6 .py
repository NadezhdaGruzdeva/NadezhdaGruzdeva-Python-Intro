# 6. Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

#lets 1 it's Monday. 
# So 6 and are days off
weekDay = int(input('Введите цифру, обозначающую день недели от 1 до 7: '))
weekDay_list = [1, 2, 3, 4, 5, 6, 7]
if weekDay not in weekDay_list:
    print('Вы ввели не целое число от 1 до 7')
elif weekDay == 6 or weekDay == 7:
    print(f'The day № {weekDay} is a day off')
else:
    print(f'The day № {weekDay} is a workday')