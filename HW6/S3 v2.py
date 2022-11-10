# 20.  Вывести список, содержащий средние арифметические значения чисел 
# каждого вложенного кортежа в заданном кортеже кортежей numbers.
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

my_list = [sum(i)/len(i) for i in numbers] #list comprehension с изменением
# my_list = []
# for i in range (len(numbers)):
#     my_list.append(sum(numbers[i]) / len(numbers[i]))

print(my_list)



