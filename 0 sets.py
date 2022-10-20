numbers = {2, 4, 6, 8, 10}
languages = {'yellow', 'green', 'blue',}

my_set = {'green', 12345, 61.5}

my_set = set()
print(type(my_set))
my_set = {}
print(type(my_set))

'''
Множества не могут содержать повторяющиеся элементы. 
Если в функцию set() передать аргумент, содержащий повторяющиеся элементы, 
то в множестве появится только один из этих повторяющихся элементов.
'''

myset1 = {2, 2, 4, 6, 6}
myset2 = set([1, 2, 2, 3, 3])
myset3 = set('aaaaabbbbccccddd')

print(myset1)
print(myset2)
print(myset3)

myset = set('Мама мыла раму')

print(myset)


myset = set(['Мама', 'мыла', 'раму'])

print(myset)


myset1 = {1, 2, ['aaa', 'bbbb', 'cc'], 7}
print(myset1) #unpossible include list in sets


'''
Для добавления нового элемента в множество используется метод add().
'''

numbers = {1, 1, 2, 3, 5, 8, 3}
print(numbers)

numbers.add(123)
numbers.add(234)
numbers.add(5)

print(numbers)

'''
Метод remove() — удаляет элемент из множества. При отсутствии элемента - ошибка.
'''

numbers = {1, 2, 3, 4, 5}

numbers.remove(3)
print(numbers)

'''
Метод discard() — удаляет элемент из множества без генерации исключения (ошибки), если элемент отсутствует.
'''


numbers = {1, 2, 3, 4, 5}

numbers.discard(3)
print(numbers)


numbers = {1, 2, 3, 4, 5}

numbers.discard(10)
print(numbers)

'''
Метод pop() — удаляет и возвращает случайный элемент из множества
Gри попытке удаления из пустого множества - исключение (ошибка) .
'''

numbers = {1, 2, 3, 4, 5}

print('до удаления:', numbers)
num = numbers.pop()
print('удалённый элемент:', num)
print('после удаления:', numbers)

'''
Метод clear() удаляет все элементы из множества.
'''


numbers = {1, 2, 3, 4, 5}
numbers.clear()

print(numbers)

