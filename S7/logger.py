from datetime import datetime as dt
from view import mode

def general_log(num1, num2, func, res):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Время внесения данных {time}, Число первое = {num1}, Число второе = {num2}, {mode[func]}, Результат = {res} \n')
