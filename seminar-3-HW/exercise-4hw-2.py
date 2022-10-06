# 2.	Напишите программу, которая найдёт произведение пар чисел списка. Парой
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
from random import randint as RI


def create_list(num, start_num, end_num):
    return [RI(start_num, end_num) for i in range(num)]


def multip_list_elem(new_list):
    midd = math.ceil(len(new_list)/2)
    return [new_list[i]*new_list[-i-1] for i in range(midd)]
    # midd = int(len(my_list)/2)
    # print(midd)
    # if len(my_list) % 2 == 0:
    #     for i in range(1, midd):
    #         print(i)
    #         result_list[i-1] = my_list[i-1]*my_list[(-i)]
    #         print(result_list[i-1])
    # else:
    #     for i in range(1, midd-1):
    #         print(i)
    #         result_list[i-1] = new_list[i-1]*new_list[(-i)]
    #     # result_list.append(new_list[midd]**2)
    # return result_list


print('Создадим исходный список случайным способом')
number = int(input('Введите количество элементов списка: '))
start = int(input('Введите начало случайного ряда: '))
end = int(input('Введите окончание случайного ряда: '))
new_list = create_list(number, start, end)
print(new_list)
print(multip_list_elem(new_list))
