# 3.	Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform as UF


def create_list(num, start_num, end_num):
    return [round(UF(start_num, end_num), 1) for i in range(num)]

def diff_list_elem(new_list):
    frac=[round(i-int(i),1) for i in (new_list)]
    difference= max(frac)-min(frac)
    return difference

print('Создадим исходный список случайным способом')
number=int(input('Введите количество элементов списка: '))
start=int(input('Введите начало случайного ряда: '))
end=int(input('Введите окончание случайного ряда: '))
new_list=create_list(number, start, end)
print(new_list)
diff=diff_list_elem(new_list)
print(diff)
