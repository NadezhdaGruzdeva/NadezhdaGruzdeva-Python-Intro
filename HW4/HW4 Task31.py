# 31. Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

n = int(input('Задайте натуральное число '))
my_list = [1]
if_simple = True

for i in range(2, int(n/2) + 1):
    for j in range (2, i):
        if i % j == 0:
            if_simple = False
            break
        else:
            if_simple = True
    if n % i == 0 and if_simple == True:
        my_list.append(i)
print(my_list)