# 1.	Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI

def create_list(num, start_num, end_num):
    return [RI(start_num, end_num) for i in range(num)]

def odd_sum(new_list):
    result = sum(new_list[1::2])
    return result

print('Создадим исходный список случайным способом')
number = int(input('Введите количество элементов списка: '))
start = int(input('Введите начало случайного ряда: '))
end = int(input('Введите окончание случайного ряда: '))
new_list = create_list(number, start, end)
print(new_list)
sum_result=odd_sum(new_list)
print(sum_result)

