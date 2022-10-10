# 2.	Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def create_list(num):
    new_list = []
    for i in range(2, num+1):
        while num % i == 0:
            new_list.append(i)
            num //= i
    return new_list

num = int(input('Введите натуральное число N: '))
my_list=create_list(num)
print(my_list)