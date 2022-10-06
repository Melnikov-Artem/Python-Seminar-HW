# 5.	Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def rec_fibo(numfib):
    if numfib in [1, 2]:
        return 1
    elif numfib == 0:
        return 0
    else:
        return rec_fibo(numfib-1)+rec_fibo(numfib-2)


def creat_fibo(num):
    row_fibo = []
    for i in range(1, num+1):
        row_fibo.append(rec_fibo(i))
    return row_fibo


print('Будет сформирован ряд Фибоначчи ->')
number = int(input('Введидете число:'))
row_fibo = creat_fibo(number)
print(row_fibo)

l = len(row_fibo)
result_fibo = []
for i in range(0, l):
    n = row_fibo[l-1-i]
    result_fibo.append(n)
print(result_fibo)
for i in range(0,l):
    print(i)
    if (i%2)!=0:
        result_fibo[-(i+1)]=-result_fibo[-(i+1)]
result_fibo.append(0)
for j in range(0, l):
    n = row_fibo[j]
    result_fibo.append(n)
print(result_fibo)