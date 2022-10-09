# 3. Задайте список из n чисел последовательности
# (1+1/n)^n выведите на экран их сумму.

def number_list(N):
    return [round((1+1/i)**i, 2) for i in range(1, N+1)]


n = int(input('Введите число N: '))
num_list = number_list(n)
print(f'Исходный список: {num_list}')
print(f'Сумма чисел: {sum(num_list)}')
