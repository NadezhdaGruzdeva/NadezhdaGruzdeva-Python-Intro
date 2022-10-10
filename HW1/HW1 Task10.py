# 10. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21


x1 = int(input('Enter X of point 1 \n'))
y1 = int(input('Enter Y of point 1 \n'))
x2 = int(input('Enter X of point 2 \n'))
y2 = int(input('Enter Y of point 2 \n'))

distance =(((x1 - x2) ** 2 + (y1 - y2) ** 2)) ** 0.5
print(f'Расстояние между точками = {distance:.2f}')