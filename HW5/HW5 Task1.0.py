# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета (input qty). 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

import random
print('Привет! Добро пожаловать в игру с конфетами.')
print('\033[35mПравила игры: \n\033[0mИграют два игрока делая ход друг после друга.\
    \nЗа один ход можно забрать не более чем 28 конфет.\
    \nВсе конфеты оппонента достаются сделавшему последний ход.')

# gamerName1 = input('Введите имя 1-ого игрока ')
# gamerName2 = input('Введите имя 2-ого игрока ')
gamer1 = 'Владимир Путин'
gamer2 = 'Владимир Зеленский'

# sweetsQty = int(input('Сколько конфет положим на кон? '))
sweetsQty = 100

maxTeakeSwets = 28
firstTurn = random.randint(1,2)
if firstTurn == 1:
    currentTurn = gamer1
else:
    currentTurn = gamer2
print(f'Первым ходит игрок \033[35m{currentTurn}\033[0m')

while sweetsQty > 0:
    print(f'Сейчас на столе \033[32m{sweetsQty}\033[0m конфет')
    takeSwets = int(input(f'\033[35m{currentTurn}\033[0m, сколько конфет вы забираете (от 1 до {maxTeakeSwets})? '))
    if takeSwets not in range(1, maxTeakeSwets + 1) or takeSwets > sweetsQty:
        print('Увы,столько конфет взять нельзя.')
        continue
    sweetsQty = sweetsQty - takeSwets
    if currentTurn == gamer1:
        currentTurn = gamer2
    else:
        currentTurn = gamer1
else:
    if currentTurn == gamer1:
        print(f'В данной битве за сладости победил: \033[35m{gamer2}\033[0m')
    else:
        print(f'В данной битве за сладости победил: \033[35m{gamer1}\033[0m')
print('И да, лучше бы они играли в конфеты.')
