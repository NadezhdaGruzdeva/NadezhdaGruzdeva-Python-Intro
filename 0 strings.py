'''
Метод .split()
Первая задача: дан адрес “https://geekbrains.ru/teacher/lessons/79615”. Нужно его распарсить — придать определённую структуру, понять, что есть что.
Обычно при парсинге начинают с разделения исходной строки на части по определённой схеме. В нашем примере очевидно, что надо делить по слешу:
url = 'https://geekbrains.ru/teacher/lessons/79615'
url_parts = url.split('/')
print(url_parts)
# ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']
'''
url = 'https://geekbrains.ru/teacher/lessons/79615'
url_parts = url.split('/')
print(url_parts)
# ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']

url = 'https://geekbrains.ru/teacher/lessons/79615'
_t_protocol, _, domain, *resource_address = url.split('/')
t_protocol = _t_protocol[:-1]
print(t_protocol, resource_address)


'''
.join()
!!! он корректно склеивает последовательности, состоящие только из строк
'''
raw_url = ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']
print('/'.join(raw_url))

url = '/'.join(raw_url)
print(url)


raw_url_2 = ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', 79615]
url_2 = '/'.join(raw_url_2)
print(url_2)

'''
.upper() и .lower() — вся строка переводится в верхний или нижний регистр:
'''
msg = 'Товаров в корзине: 5'
print(msg.upper())
#
print(msg.lower())

print(msg.upper())  # ТОВАРОВ В КОРЗИНЕ: 5
print(msg.lower())  # товаров в корзине: 5

'''
Правим регистр: методы .title() и .capitalize() — либо у всех слов первая буква становится заглавной, либо только первая:
'''

 

'''
Реверс строк
Для реверса строк используем срез с шагом -1:
'''

msg = 'а роза упала на лапу Азора'
#
#
#
print(msg[::-1])





# print(msg[::-1])  # арозА упал ан алапу азор а
