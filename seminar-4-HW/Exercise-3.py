# 3.Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint as RI


def create_list(n, st, end):
    return [RI(st, end) for i in range(n)]


def unic_list(n_list):
    new_list=[]
    double_list=[]
    for i in range(len(n_list)-1):
        if n_list[i] not in double_list:
            count=0
            for j in range(i+1,len(n_list)):
                if n_list[i]==n_list[j]:
                    count+=1
            if count==0:
                new_list.append(n_list[i])
            else:
                double_list.append(n_list[i])
    return new_list


print('Создадим последовательность случайных чисел.\n')
num_size = int(input('Определите размер последовательности N: '))
num_start = int(input('Введите начало случайной последовательности: '))
num_end = int(input('Введите окончание случайной последовательности: '))
random_list = create_list(num_size, num_start, num_end)
print(f'\nИсходная последовательность: {random_list}\n')
print(f'Последовательность из неповторяющихся элементов: {set(random_list)}')
new_list = unic_list(random_list)
print(f'Последовательность из уникальных элементов: {new_list}\n')
