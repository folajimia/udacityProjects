import os

def rename_files():
	file_list = os.listdir(r"C:\prank")
	print(file_list)
	saved_path = os.getcwd()
	print("Current working Directory is "+saved_path)
	os.chdir(r"C:\prank")

	for file_name in file_list:
		print("old name of file -" + file_name)
		print("New name of file -" + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789") )
	os.chdir(saved_path)

rename_files()

