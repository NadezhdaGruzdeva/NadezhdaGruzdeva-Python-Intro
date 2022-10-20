my_list = [1, 2, 3, 4, 5]
my_list[0] = 9
my_list[4] = 7
print(my_list)


my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 9
my_tuple[4] = 7
print(my_tuple)


my_tuple = (1,)
print(type(my_tuple))

my_tuple = (1, 'python', [1, 2, 3])
print(my_tuple)
my_tuple[2][0] = 100
my_tuple[2].append(17)
print(my_tuple)


a = (3, 4, 5)
for i in range(3):
    a[i] += 3
print(sum(a))


colors = ('red', ('green', 'blue'), 'yellow')
numbers = (1, 2, (4, (6, 7, 8, 9)), 10, 11)
print(colors[1][1])
print(numbers[2][1][3])
print(type(colors))
print(type(numbers))


letters = 'abcdefghijkl'
tpl = tuple(letters)
print(tpl)



number = 12345
tpl = tuple(number)
print(tpl)


'''
Метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению.
Таким образом, в метод передается один параметр:
value: значение, индекс которого требуется найти.
Если элемент в кортеже не найден, то во время выполнения происходит ошибка.
'''
colors = ('red', 'green', 'yellow')
position = colors.index('green')
print(position)


colors = ('red', 'green', 'yellow')
position = colors.index('black')
print(position)


colors = ('red', 'green', 'yellow')
if 'black' in colors:
    position = colors.index('black')
    print(position)
else:
    print('Такого значения нет в кортеже')


'''
Метод count()
Метод count() возвращает количество элементов в кортеже, значения которых равны переданному в метод значению. 
В метод передается один параметр:

value: значение, количество элементов, равных которому,  нужно посчитать.
Если значение в кортеже не найдено, то метод возвращает 0.
'''
colors = ('red', 'green', 'white', 'yellow', 'green', 'blue', 'green')
cnt1 = colors.count('red')
cnt2 = colors.count('violet')
cnt3 = colors.count('green')

print(cnt1)
print(cnt2)
print(cnt3)

'''
Встроенная функция sum() принимает в качестве параметра кортеж чисел и вычисляет сумму его элементов.
'''

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Сумма всех элементов кортежа =', sum(numbers))

'''
Встроенные функции min() и max() принимают в качестве параметра кортеж и находят минимальный и максимальный элементы соответственно.
'''

numbers = (3, 4, 10, 3333, 12, -7, -5, 4)
print('Минимальный элемент кортежа =', min(numbers))
print('Максимальный элемент кортежа =', max(numbers))


