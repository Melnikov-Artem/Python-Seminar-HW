# 5.	Реализуйте алгоритм перемешивания списка.
# ВТОРОЙ СПОСОБ

from random import randint as RI


def create_list(Num, N_start, N_end):
    return [RI(N_start, N_end) for i in range(Num)]

def shuffle_list(my_list):
    for i in range(len(my_list)):
        j= RI(1,len(my_list))
        my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list
    

num = int(input('Введите размер списка, N: '))
n_start = int(input('Укажите начало случайного ряда: '))
n_end = int(input('Укажите окончание случайного ряда: '))
my_list = create_list(num, n_start, n_end)
print(f'Исходный список: {my_list}')
new_list=shuffle_list(my_list)
print(f'Список после перемешивания: {new_list}')