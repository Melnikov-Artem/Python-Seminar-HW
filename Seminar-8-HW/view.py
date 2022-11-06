

# показать меню
def show_menu():
	print('1 - показать всё')
	print('2 - добавить запись')
	print('3 - удалить запись')
	print('4 - обновление записи')
	return int(input('Введите номер меню:\n'))


def delete():
	print('Введите индекс для удаления')
	return int(input())


def change_info():
	print('Введите первый индекс для изменения')
	print('Введите второй индекс для изменения')
	print('Введите новую информацию')
	return int(input()), int(input()), input()

def show_result(res_list):
	for i, row in enumerate(res_list):
		print(i, ' '.join(row))

def add_info():
	print('Введите ФИО, телефон через пробел:')
	input_info = input().split()
	return input_info