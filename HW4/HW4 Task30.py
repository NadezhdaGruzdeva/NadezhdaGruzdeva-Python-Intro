# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — 
# данные об их хобби. Известно, что при хранении данных используется принцип: 
# одна строка — один пользователь. Написать код, загружающий данные из обоих файлов
#  и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи


u = open('users.txt', 'r', encoding='utf8') # opening
h = open('hobby.txt', 'r', encoding='utf8') 

users = u.readlines() #reading
hobby = h.readlines()

for i in range(len(users)): #clearing
    users[i] = users[i].replace('\n','')

for i in range(len(hobby)):
    hobby[i] = hobby[i].replace('\n','')

u.close()
h.close()

my_dict = dict(zip(users, hobby)) #concatination into dictionary
# print(dictionary)

with open('users_hobby.txt', 'w', encoding="utf-8") as out: # print dict into file (from Seminar 4)
    keys = my_dict.keys()
    for key in keys:
        out.write(f'{key}: {my_dict[key]} \n')





        


