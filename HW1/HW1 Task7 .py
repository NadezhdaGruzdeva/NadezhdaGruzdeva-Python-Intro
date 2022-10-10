# 7. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# 0 = FALSE
# 1 = TRUE

for x in range (2):
    for y in range (2):
        for z in range (2):     
            if(not (x or y or z) == (not x and not y and not z)):
                continue
            else:
                print ('Утверждение не верно')
                break #не знаю как сделать break из всех чисел
if (not(x or y or z) == (not x and not y and not z)):
    print ('Утверждение истино')