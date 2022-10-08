# 2.	Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

def factorial_list(N):
    multi_dig = 1
    fact_list = [1]
    for i in range(2, N+1):
        multi_dig *= i
        fact_list.append(multi_dig)
    return fact_list


num = int(input('Введите число факториала: '))
print(factorial_list(num))

# num_fact = factorial(num)
# print(num_fact)

# fact(int n)
# {
#     if (n < 2) return 1
#     else return n * fact(n-1)
# }

# for (int i=0
#      i < 20
#      i++)
# Console.WriteLine(fact(i))
