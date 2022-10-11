# 7. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# 0 = FALSE
# 1 = TRUE
def func():
    for x in range (2):
        for y in range (2):
            for z in range (2):     
                if(not (x or y or z) == (not x and not y and not z)):
                    continue
                else:
                    return print ('Утверждение не верно')
                    # break #не знаю как сделать break из всех чисел
    if (not(x or y or z) == (not x and not y and not z)):
        return print ('Утверждение истино')
func()

# для проверики ложного
# def func():
#     for x in range (2):
#         for y in range (2):
#             for z in range (2):     
#                 if((x or y or z) == (not x and not y and not z)):
#                     continue
#                 else:
#                     return print ('Утверждение не верно')
#                     # break #не знаю как сделать break из всех чисел
#     if ((x or y or z) == (not x and not y and not z)):
#         return print ('Утверждение истино')
# func()