# 5.	Реализуйте алгоритм перемешивания списка.

from random import randint as RI
from random import shuffle as SH


def create_list(Num, N_start, N_end):
    return [RI(N_start, N_end) for i in range(Num)]


num = int(input('Введите размер списка, N: '))
n_start = int(input('Укажите начало случайного ряда: '))
n_end = int(input('Укажите окончание случайного ряда: '))
my_list = create_list(num, n_start, n_end)
print(my_list)
SH(my_list)
print(my_list)
