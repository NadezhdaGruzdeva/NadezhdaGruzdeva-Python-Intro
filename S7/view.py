def get_value():
    value_a = int(input('value_a = '))
    value_b = int(input('value_b = '))
    return value_a, value_b


def get_mode():
    mode = input('Введите интересующую вас операцию(нацело или с остатком): ')
    if mode.lower() == 'нацело':
        return 1
    elif mode.lower() == 'с остатком':
        return 2
    else:
        print ("You've entered incorrect value")
mode = {1: 'результат деления нацело', 2:'остаток от деления'}
def return_result(res, oper):
    return f'Result of action {mode[oper]}= {res}'