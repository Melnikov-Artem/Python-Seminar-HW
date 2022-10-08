# Дополнительно ко 2-му заданию (РЕКУРСИЯ).
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

fact_list = []


def factorial_rec_list(n):
    if n < 2:
        fact_list.append(1)
        return 1
    else:
        fact_list.append((n-1)*(n))
        return n*factorial_rec_list(n-1)


num = int(input('Введите число факториала: '))
print(factorial_rec_list(num))
print(f'Список факториала: {fact_list[::-1]}')
