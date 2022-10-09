# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
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

# result[::-1]
# result = ''.join(reversed(result))


def create_file_pol1(path_file, pol):
    with open(path_file, 'w') as f_data:
        f_data.write(pol)


num_k = int(input('Введите степень многочлена k: '))
kf_pol_list = create_koef_polinom(num_k)
print(f'Koэффициенты многочлена: {kf_pol_list}')
polinom = create_polinom(num_k, kf_pol_list)
print(f'Сформированный многочлен: {polinom}')
path_file = '.\Seminar-4-HW\polinom-1.txt'
create_file_pol1(path_file, polinom)
