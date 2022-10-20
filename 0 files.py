# import homework_3
# print(homework_3.fib(8))



'''
Методы файлов
file.closed	возвращает истину (True), если файл закрыт, иначе возвращает ложь (False)
file.mode	возвращает режим доступа с помощью которого был открыт файл
file.name	возвращает имя файла

1
r, w, x, a
2
t, b
3
+
http://phpfaq.ru/newbie/paths - пути относительный и абсолютный
'''

'''
Для чтения используются методы:
read() – читает все содержимое файла;
readline() – читает одну строку из файла;
readlines() – читает все содержимое файла и возвращает список строк.
'''

file_1 = open('hello.txt', 'r', encoding='utf8')
content = file_1.read()
print(content)
print(file_1.closed)
file_1.close()
print(file_1.closed)

'''
read читает «сырой» текст вместе с управляющими символами “\n”, ”\r” и другими https://ru.wikipedia.org/wiki/%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B5_%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B
.replace('\n', ' ')
.replace('\r', ' ')
encoding='utf-8'
Перемещение курсора при работе с файлом: .seek() и .tell()
'''

clean_content = content.replace('\n', ' ').replace('\r', ' ')
print(clean_content)

paragraphs = content.splitlines()
print(paragraphs)


file_1 = open('hello.txt', 'r', encoding='utf-8')
paragraphs = file_1.readlines()
print(paragraphs)
file_1.close()

file_1 = open('hello.txt', 'r', encoding='utf-8')
print(file_1.readline())
print(file_1.readline())
file_1.close()

# # '''Режим построчного чтения'''
file_1 = open('hello.txt', 'r', encoding='utf-8')
line = file_1.readline()
while line:
    print(line)
    line = file_1.readline()
file_1.close()

with open('hello.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        print(line)
    print(file_1.closed)
print(file_1.closed)

'''
Для записи используются два файловых метода:
write() – записывает переданную строку в файл;
writelines() – записывает переданный список строк в файл.
'''

my_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}
print(my_dict)

# with open('test.txt', 'w') as out:
#     out.writelines(' '.join(my_dict))


# with open('test.txt', 'w') as out:
#     for key, val in my_dict.items():
#         out.write('{}: {}\n'.format(key, val))

keys = my_dict.keys()
f = open("test.txt", "a")
for key in keys:
    f.write(f'{key}: {my_dict[key]} \n')
#
print(f.closed)
f.close()
print(f.closed)


with open('test1.txt', 'w') as f:
    for key, value in my_dict.items():
        f.write(f'{key}: {value}\n')
    print(f.mode)
    print(f.closed)
print(f.closed)

#
#
#
my_list = ['first string', 'second string', 'third string', 'fourth string', 'fifth string']

with open('test2.txt', 'w') as my_file:
    my_file.writelines(my_list)
    print(my_list, sep='\n', file=my_file)

with open('test2.txt', 'w') as my_file:
    for line in my_list:
        my_file.writelines(line+'\n')

#
#
#
with open('test2.txt', 'a') as my_file:
    for element in my_list:
        print(element, sep='\n', file=my_file)


with open('test2.txt', encoding='utf-8') as f:
    text = f.read().replace('\n', ' ')
print(text)
