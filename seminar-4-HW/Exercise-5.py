# 5.Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint as RI


def create_koef_polinom(k):
    kp_list = [RI(0, 100) for i in range(k+1)]
    if kp_list[0] == 0:
        kp_list[0] = RI(1, 100)
    return kp_list


def create_polinom(k, kf_list):
    result = ''
    str_elem = ''
    for i in range(k+1):
        str_elem = str(kf_list[i])+'*x^'+str(k-i)
        if i == 0:
            result = str_elem
        elif kf_list[i] != 0:
            result = result + ' + '+str_elem
    result = result.replace('*x^0', '')
    result = result.replace('x^1', 'x')
    result = result.replace(' 1*x', ' x')
    result = result + ' = 0'
    return result


def sum_2polinom(pol1, pol2, k1, k2):
    if k1>k2:
        koef_max=k1
        for i in range(k1+1):
            pol_sum_list.append(pol1[i])
        for i in range(k2+1):
            pol_sum_list[len(pol_sum_list)-1-i]+=pol2[k2-i]
    else:
        koef_max=k2
        for i in range(k2+1):
            pol_sum_list.append(pol2[i])
        for i in range(k1+1):
            pol_sum_list[len(pol_sum_list)-1-i]+=pol1[k1-i]
    return koef_max


def create_file_pol1(path_file, pol):
    with open(path_file, 'w') as f_data:
        f_data.write(pol)


num_k_1 = int(input('Введите степень 1-го многочлена k1: '))
num_k_2 = int(input('Введите степень 2-го многочлена k2: '))
kf_pol_list_1 = create_koef_polinom(num_k_1)
kf_pol_list_2 = create_koef_polinom(num_k_2)
print(f'\nKoэффициенты 1-го многочлена: {kf_pol_list_1}')
print(f'Koэффициенты 2-го многочлена: {kf_pol_list_2}\n')
polinom_1 = create_polinom(num_k_1, kf_pol_list_1)
polinom_2 = create_polinom(num_k_2, kf_pol_list_2)
print(f'\nСформированный 1-й многочлен: {polinom_1}')
print(f'Сформированный 2-й многочлен: {polinom_2}\n')

pol_sum_list = []
koef_max = sum_2polinom(kf_pol_list_1, kf_pol_list_2, num_k_1, num_k_2)

polinom_sum = create_polinom(koef_max, pol_sum_list)
print(f'\nСумма 2-х многочленов: {polinom_sum}\n')
path_file = '.\Seminar-4-HW\polinom-sum.txt'
create_file_pol1(path_file, polinom_sum)
