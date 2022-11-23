import operations_rational as op
import sys

def x():
    firstnum = float(input('Choose first float number: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Choose second float number: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Select operation: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Invalid syntax')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('invalid syntax')

def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'The result of {x} {oper} {y} = {res}\n')
        print(f'The result of {x} {oper} {y} = {res}\n(already written to txt file)' )
        again = input('Do you want calculate another numbers? Yes/No: ').lower()
        if again == 'yes':
            useresult = input('Do you want to use the result of the last operation? (Yes/No): ').lower()
            if useresult == 'yes':
                x = res
                continue
            elif useresult == 'no':
                break
            else:
                sys.exit()           
        else:   
            sys.exit()