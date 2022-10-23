# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def ToHash(full_str):
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

    print(f"\033[33m{full_str}\033[0m - The hash string" )
    print(f"\033[33m{hash_str}\033[0m - The hash string")
    return hash_str

def ToFull(hash_str):
    full_str = ''
    i = 0
    fig = 0
    isComplex = False
    while i < len(hash_str):
        if hash_str[i] in '0123456':
            isComplex = True
            fig = int(hash_str[i])
        elif isComplex == True:
            full_str += fig * hash_str[i]
            isComplex = False
        else:
            full_str += hash_str[i]
        i += 1
    print(f"\033[33m{hash_str}\033[0m - The hash string")
    print(f"\033[33m{full_str}\033[0m - The hash string" )
    return full_str

with open('hw5 InitialText.txt', 'r', encoding='utf-8') as full:
    my_str = full.read()
with open('hw5 hash.txt', 'w', encoding='utf-8') as hash:
    hash.write(ToHash(my_str))

with open('hw5 hash.txt', 'r', encoding='utf-8') as hash:
    my_str = hash.read()
with open('hw5 InitialText.txt', 'w', encoding='utf-8') as full:
    full.write(ToFull(my_str))