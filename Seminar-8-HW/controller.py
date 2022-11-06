import model
import view

def run ():
	start = view.show_menu()
	if start == 1: 
		res = model.csv_data_open()
		view.show_result(res)
	elif start == 2:
		input_info=view.add_info()
		model.add_info(input_info)
	elif start == 3:
		index = view.delete()
		model.delete_info(index)
	elif start == 4:
		up_info = view.change_info()
		model.update_info(up_info)