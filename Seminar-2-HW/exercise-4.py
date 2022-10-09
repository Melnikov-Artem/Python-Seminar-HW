# 4.Задайте числами список из N элементов,
# заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint as RI


def create_number_list(N):
    return [RI(-i, i) for i in range(1, N+1)]


def create_file(path, N, num):
    with open(path, 'w') as f_data:
        for i in range(1, N+1):
            f_data.write(f'{RI(0,num)}\n')


def create_multlist(path, N):
    mult_list = []
    with open(path, 'r') as f_data:
        for i in f_data.readlines():
            mult_list.append(i.strip())
    return mult_list


def result_mult(num_list, multlist):
    mult_number = 1
    for i in multlist:
        mult_number *= num_list[int(i)]
    return mult_number


n = int(input('Введите для диапазона число N: '))
# path_file = input('Укажите имя (путь файла): ')
path_file = '.\Seminar-2-HW\mult_string.txt'
num_str = int(input('Укажите количество строк в файле): '))
num_list = create_number_list(n)
print(f'Исходный список: {num_list}')
create_file(path_file, num_str, n)
multlist = create_multlist(path_file, num_str)
print(f'Список номеров элементов из файла: {multlist}')
multnumber = result_mult(num_list, multlist)
print(f'{multnumber}')
