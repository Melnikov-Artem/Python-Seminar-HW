#4.Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).

from sys import setswitchinterval


print('\n')
numQuater = int(input('Введите номер четверти: '))
if 0 < numQuater < 5 :
    print('Диапазон возможных координат')
    if numQuater == 1: print('X > 0 и Y > 0')
    elif numQuater == 2: print('X < 0 и Y > 0')
    elif numQuater == 3: print('X < 0 и Y < 0')
    else: print('X > 0 и Y < 0')
else: print(f'ОШИБКА!\nНомер четверти={numQuater} не существует!')
print('\n')