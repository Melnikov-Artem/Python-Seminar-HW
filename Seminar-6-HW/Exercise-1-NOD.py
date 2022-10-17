# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.
# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод
# чисел продолжается до ввода пустой строки.
from math import gcd
from functools import reduce


def mess_data_print(mes):
    return input(mes)


def get_list_num():
    message_error = "Ошибка! Введите число."
    valid = False
    num_lst = []
    while not valid:
        num_input = mess_data_print('Введите следующее число: ')
        try:
            if num_input != '':
                num_lst.append(int(num_input))
            else:
                valid = True
        except:
            print(message_error)
            continue      
    return num_lst


def calc_gcd(num_lst):
    return reduce(gcd, num_lst)


message_start = '\nВведите набор чисел по очериди для определения НОД.\n\
Вычисление произойдёт после ввода пустой строки.\n'

print(message_start)

num_lst = get_list_num()
print(f'\nНОД, введёных Вами чисел: {calc_gcd(num_lst)}\n')