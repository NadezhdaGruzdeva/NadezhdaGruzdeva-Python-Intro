from binascii import crc32


print ('hello world')

value = None
a = 123
b = 1.23
s= 'hello world'
t= 'hello \n world'
f= True
list = [1, 2, 3, 4]

# Print type
print(type(a))
print(type(b)) 
print(type(value))
print(type(s))
print(type(t))
print(type(f))
print(type(list))

# Print value
print(a)
print(b) 
print(value)
print(s)
print(t)
print(f)
print(list)
print(a, b, s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

#ввод и вывод данных print input
print ('Enter c')
c = input() # так бедет вводится как строка
print(type(c))
print ('Enter d')
d = int(input()) # так бедет вводится как число
print(type(d))
print ('c = ', c)
print ('d = ', d)
# print ('c + a = ', c + a)
print (d, ' + ', a, '= ', d + a)

a = int(input('Введите \nа: '))
b = int(input('Введите \nb: '))
c = a + b
print('{} + {} = {}'.format(a, b, c))

#  арифметические операции
k = 2
l = 9
m = k * l 
o = l // k
p = l ** k
print(m)
print(o)
print (p)

#Логические операции
q = 1 < 4 < 5 and 5 > 2
print(q)

r = 'qwe'
s = 'qwe'
print (r == s)

t = [1,2,3,4]
print (not 5 in t)

#is_odd = t [0] % 2 == 0
is_odd = not t [0] % 2  #the same так ка 0 -ложь, 1 -истина
print (is_odd)

# if else 
username = input('Введите имя: ')
if(username == 'Маша'):
 print('Ура, это же МАША!')
else:
 print('Привет, ', username)

 ## if else elif
username2 = input('Введите имя: ')
if username2 == 'Маша':
 print('Ура, это же МАША!')
elif username2 == 'Марина':
 print('Я так ждала Вас, Марина!')
elif username2 == 'Ильнар':
 print('Ильнар - топ)')
else:
 print('Привет, ', username2)

 # while
original = 236
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
print(inverted)

# while else
original = 2366
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
else:
 print('Пожалуй')
 print('хватит )')
print(inverted)

#for
for i in 1, -2, 3, 14, 5:
    print(i)

r = range(5) # range(0,5)
r = range(2, 5) # range(2, 5)
r = range(-5, 0) # range(-5, 0)
r = range(1, 10, 2) # range(1, 10, 2)
r = range(100, 0, -20) # range(100, 0, -20)

for i in range(100, 0, -20): #от 100 до 0 с шагом -20
 print(i)
# 100 80 60 40 20

for i in range(5):
 print(i)
# 0 1 2 3 4


# Вложенные циклы
line = ""
for i in range(5):
  line = ""
  for j in range(5):
    line += "*"
    print(line)

# Немного о строках 
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False

print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #

# Немного о строках срезы
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text) print(text[0:len(text)-1])
print(text[:2]) # съ [0:2]
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
print(type(numbers))
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]


# Списки: введение
colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент.

# Functions 
def f(x):
 return x**2

def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return

arg =2
print(f(arg))
print(type(f(arg)))

#Справки по функциям
help(str) 