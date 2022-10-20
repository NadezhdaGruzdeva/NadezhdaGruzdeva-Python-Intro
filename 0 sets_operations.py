'''
Объединение множеств union()
возвращает новое множество в которое входят все элементы объединенных множеств.
Для объединения двух множеств можно также использовать оператор |
Для изменения текущего множества используется метод update()
'''

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.union(myset2)
# print(myset3)


# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 | myset2
# print(myset3)


'''
Пересечение множеств: метод intersection()
Метод intersection() возвращает новое множество, в которое входят общие элементы множеств.
Для изменения текущего множества используется метод intersection_update()
Для пересечения двух множеств можно также использовать оператор &.
'''

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.intersection(myset2)
# print(myset3)


# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 & myset2
# print(myset3)

'''
Разность множеств: метод difference() возвращает множество, в которое входят все элементы первого множества, не входящие во второе множество. 
Для разности двух множеств можно также использовать оператор -.
!!! Для операции разности множеств важен порядок, в котором указаны множества. Если поменять местами myset1 и myset2, получим совсем другой результат: 
элементы входящие в множество myset2 и которых нет в множестве myset1.
'''

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.difference(myset2)
# print(myset3)


# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 - myset2
# print(myset3)



# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset2.difference(myset1)
# print(myset3)



'''
Симметрическая разность: symmetric_difference()
Возвращает множество, включающее все элементы исходных множеств, не принадлежащие одновременно обоим исходным множествам. 
Для симметрической разности двух множеств можно также использовать оператор ^.
'''

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1.symmetric_difference(myset2)
# print(myset3)

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset3 = myset1 ^ myset2
# print(myset3)

'''
Метод update() изменяет исходное множество по объединению.
Аналогичный результат получается, если использовать оператор |=:
'''

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.update(myset2)
# print(myset1)



# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1 |= myset2
# print(myset1)

'''
Метод intersection_update() изменяет исходное множество по пересечению.
Аналогичный результат получается, если использовать оператор &=:
'''


# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.intersection_update(myset2)
# print(myset1)


# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1 &= myset2
# print(myset1)


'''
Метод difference_update() изменяет исходное множество по разности.
Аналогичный результат получается, если использовать оператор -=
'''


# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.difference_update(myset2)
# print(myset1)



# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1 -= myset2
# print(myset1)

'''
Метод symmetric_difference_update() изменяет исходное множество по симметрической разности.
Аналогичный результат получается, если использовать оператор ^=:
'''

# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1.symmetric_difference_update(myset2)
# print(myset1)



# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
#
# myset1 ^= myset2
# print(myset1)





# mylist = [2021, 2020, 2019, 2018, 2017, 2016]
# mytuple = (2021, 2020, 2016)
# mystr = 'abcd'
#
# myset = {2009, 2010, 2016}
#
# print(myset.union(mystr))
# print(myset.intersection(mylist))
# print(myset.difference(mytuple))




# mylist = [2021, 2020, 2019, 2018, 2017, 2016]
# mytuple = (2021, 2020, 2016)
# mystr = 'abcd'
#
# myset = {2009, 2010, 2016}
#
# print(myset | mystr)
# print(myset & mylist)
# print(myset - mytuple)





# myset1 = {1, 2, 3, 4, 5, 6}
# myset2 = {2, 3, 4, 5}
# myset3 = {5, 6, 7, 8}
#
# union1 = myset1.union(myset2, myset3)
# union2 = myset1 | myset2 | myset3
#
# difference1 = myset1.difference(myset2, myset3)
# difference2 = myset1 - myset2 - myset3            # порядок выполнения слева-направо
#
# print(union1 == union2)
# print(difference1 == difference2)



# myset1 = {1, 2, 3, 4, 5, 6}
# myset2 = {2, 3, 4, 7}
# myset3 = {6, 20, 30}
#
# symdifference = myset1 ^ myset2 ^ myset3  # порядок выполнения слева-направо
#
# print(symdifference)



# myset1 = {1, 2, 3, 4, 5, 6}
# myset2 = {2, 3, 4, 7}
# myset3 = {6, 20, 30}
#
# symdifference = myset1.symmetric_difference(myset2, myset3)
#
# print(symdifference)