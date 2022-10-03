# ; 1.	Напишите программу, которая принимает на вход вещественное число
# ; и показывает сумму его цифр.
# ; Пример:
# ; o	6782 -> 23
# ; o	0,56 -> 11

number = float(input('Введите вещественное число: '))
res = 0
# print(0.56/2)
# print(0.56 % 1)
# print(0.56//1)
while (number//1) != 0:
    res = res + number % 10
    number = number//10
    print(f'number={number}')
    print(f'res={res}')
if (number % 1) != 0:
    ostatok=str(number)
    print(ostatok)
    for i in range (2,len(ostatok)):
        print(f'ostatok={ostatok[i]}')
        res = res+int(ostatok[i])
print(f'res={res}')
