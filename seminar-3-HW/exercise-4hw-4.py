# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# def dec_to_binary(num):
#     result = ''
#     while num > 1:
#         result=result+str(num%2)
#         num=num//2
#     return result[::-1]6


def dec_to_binary(num):
    result = ''
    while num > 0:
        result = result + str(num % 2)
        num = num//2
    result = ''.join(reversed(result))
    return result


number = int(input('Введите десятичное число: '))
bin_number = dec_to_binary(number)
print(f'Десятичное число: {number} в двоичной системе: {bin_number}')
