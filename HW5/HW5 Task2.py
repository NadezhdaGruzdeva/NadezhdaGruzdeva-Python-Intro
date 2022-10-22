# 2. Создайте программу для игры в ""Крестики-нолики"".

# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
with open(r'C:\Users\Nadezhda\Desktop\Geek Brains\Python introduction\HW5\hw5 InitialText.txt', 'r', encoding='utf-8') as full:
    full_str = full.read()

hash_str = ''
# print(type(full_str))
i = 0
qty = 1
ifAddFig = False
while i < len(full_str):
    if  i != len(full_str) - 1 and full_str[i] == full_str[i + 1]:
    #при невыполнение первого условия, программа не смотрит на второе - что круто в нашем случае
        qty += 1
        ifAddFig = True
    elif ifAddFig == True:
        hash_str += str(qty) + full_str[i]
        qty = 1
        ifAddFig = False
    else:
        hash_str += full_str[i]
    i += 1

print(full_str)
print(hash_str)