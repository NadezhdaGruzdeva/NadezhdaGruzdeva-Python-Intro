# б) Наделяем бота интеллектом

import random
print('Привет! Добро пожаловать в игру с конфетами.')
print('\033[35mПравила игры: \n\033[0mИграют два игрока делая ход друг после друга.\
    \nЗа один ход можно забрать не более чем 28 конфет.\
    \nВсе конфеты оппонента достаются сделавшему последний ход.')

# gamer1 = input('Введите имя 1-ого игрока ')
gamer1 = 'Реальный юзер'
bot = 'Кремлебот'

# sweetsQty = int(input('Сколько конфет положим на кон? '))
sweetsQty = 100

maxTeakeSwets = 28
firstTurn = random.randint(1,2)
if firstTurn == 1:
    currentTurn = gamer1
else:
    currentTurn = bot
print(f'Первым ходит игрок \033[35m{currentTurn}\033[0m')

while sweetsQty > 0:
    print(f'Сейчас на столе \033[32m{sweetsQty}\033[0m конфет')
    if currentTurn == gamer1:
        takeSwets = int(input(f'\033[35m{currentTurn}\033[0m, сколько конфет вы забираете (от 1 до {maxTeakeSwets})? '))
        if takeSwets not in range(1, maxTeakeSwets + 1) or takeSwets > sweetsQty:
            print('Увы,столько конфет взять нельзя.')
            continue
    else:
        if sweetsQty > maxTeakeSwets:
            if sweetsQty % (maxTeakeSwets + 1) == 0:
                takeSwets = random.randint(1, maxTeakeSwets)
            else:
                takeSwets = sweetsQty % (maxTeakeSwets + 1)
        else: 
            takeSwets = sweetsQty
        print(f'{bot} забрал \033[31m{takeSwets}\033[0m конфет')
    sweetsQty = sweetsQty - takeSwets
    if currentTurn == gamer1:
        currentTurn = bot
    else:
        currentTurn = gamer1
else:
    if currentTurn == gamer1:
        print(f'В данной битве за сладости победил: \033[35m{bot}\033[0m')
    else:
        print(f'В данной битве за сладости победил: \033[35m{gamer1}\033[0m')
