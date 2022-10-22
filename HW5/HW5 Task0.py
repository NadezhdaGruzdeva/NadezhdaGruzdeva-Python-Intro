# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text ="Абводной канал. Обводной канал. Абвигации федерального займа. Облигации федерального займа."

import re
next_text = re.findall(r"[\w']+|[.,!?;]", my_text) #учитываем знаки препинания (Одним split здесь не обойтись)
# print(next_text)
next_text = [el for el in next_text if 'абв' not in el.lower()]
# print(next_text)

new_text = ' '.join(next_text)

print(f'Исходный текст: \033[35m{my_text}')
print('\033[0m')
print(f'Текст без слов, содержащих "абв": \033[32m{new_text}')
print('\033[0m')