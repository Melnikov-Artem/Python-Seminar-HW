# 1.	Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

from math import pi


def calc_pi(num_infinity):
    k = 1
    x = 0
    for k in range(1, num_infinity):
        x += 4*((-1)**(k+1))/(2*k-1)
    return x


def accuracy_pi(num_d, new_pi):
    k = 0
    while num_d < 1:
        num_d *= 10
        k += 1
    return round(new_pi, k)


print('\n')
print(f'Число ПИ из математической библиотеки = {pi}\n')
print('Вычислим число ПИ по формуле бесконечного ряда.')
num_infinity = int(input('Введите число ряда (апроксимация бесконечности): '))
my_pi = calc_pi(num_infinity)
print(f'Число ПИ по формуле ряда = {my_pi}\n')
print('Теперь определим точность и округлим число ПИ.')
print('Точность числа ПИ находится в интервале: 10^(-1) ≤ d ≤10^(-10)')
num_accur = float(input('Введите точность d= '))
round_pi=accuracy_pi(num_accur, my_pi)
print(f'Округлённое число ПИ = {round_pi} с точностью d = {num_accur}')
