# 1.	Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input('Введите вещественное число: '))
res = 0
while (number//1) != 0:
    res = res + number % 10
    number = number//10
if (number % 1) != 0:
    ostatok=str(number)
    print(ostatok)
    for i in range (2,len(ostatok)):
        res = res+int(ostatok[i])
print(f'Сумма чисел = {int(res)}')
