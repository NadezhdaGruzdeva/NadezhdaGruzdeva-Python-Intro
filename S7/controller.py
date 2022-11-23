from calculation import init, devision, ostatok
from logger import general_log
from view import get_mode, get_value, return_result


def launch_rocket():
    num1, num2 = get_value()
    action = get_mode()
    init(num1, num2)
    if action == 1:
        result = devision()
    else:
        result = ostatok()
    print(return_result(result, action))
    general_log(num1, num2, action, result)


