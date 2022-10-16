#  4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def read_file(path_file, sign):
    with open(path_file, sign) as f_data:
            str_read = f_data.read()
    return str_read

def write_file(path_file, sign, str_coding):
    with open(path_file, sign) as f_data:
            f_data.write(str_coding)

def coding(str_x):
    lst = ''
    count = 1
    for i in range(0, len(str_x)-1):
        if str_x[i] == str_x[i+1]:
            count += 1
        else:
            lst = lst + ''.join(str(count)+str_x[i])
            count = 1
    lst =lst + ''.join(str(count)+str_x[i])
    return lst

def decoding(str_x):
    lst = ''
    dig = ''
    for i in range(0, len(str_x)):
        if str_x[i].isdigit():
            dig += str_x[i]
        else:
            lst = lst +''.join(str_x[i]*int(dig))
            dig = ''
    return lst


path_file_1 = '.\Seminar-5-HW\ishodnik.txt'
path_file_2 = '.\Seminar-5-HW\coding.txt'
path_file_3 = '.\Seminar-5-HW\decoding.txt'

print('---')
coder_str = read_file(path_file_1, 'r')
print(f'Исходная строка для кодирования:\n{coder_str}')

incoder_str = coding(coder_str)
write_file(path_file_2, 'w', incoder_str)
print(f'\nКодированная строка методом RLE:\n{incoder_str}\
\nЗапись сделана в файл: {path_file_2}')

decoder_str=decoding(incoder_str)
write_file(path_file_3, 'w', decoder_str)
print(f'\nРаскодированная строка:\n{decoder_str}\
\nЗапись сделана в файл: {path_file_3}\n')