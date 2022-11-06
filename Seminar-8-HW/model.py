import csv

def csv_data_open():	# 1 - показать всё
    with open("../python-begin/Seminar-8-HW/data_base.csv", encoding='utf-8') as f:
        file_csv = csv.reader(f, delimiter=";")
        res = list(file_csv)
    return res
	
def add_info(list):	# 2 - добавить запись
    with open('..\Seminar-8-HW\data_base.csv', 'a', encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)

def delete_info(index):	# 3 - удалить запись
	list_csv = csv_data_open()
	del list_csv[index]
	with open('..\Seminar-8-HW\data_base.csv', 'w', encoding="utf8", newline='') as f:
		writer = csv.writer(f, delimiter=';')
		for row in list_csv:
			writer.writerow(row)

def update_info(index_1, index_2, info):	# обновление записи
	list_csv = csv_data_open()
	list_csv[index_1][index_2] = info
	with open('..\Seminar-8-HW\data_base.csv', 'w', encoding="utf8", newline='') as f:
		writer = csv.writer(f, delimiter=';')
		for row in list_csv:
			writer.writerow(row)