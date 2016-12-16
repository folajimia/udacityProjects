import os
import random

def rename_files():
	file_list = os.listdir(r"C:\prank")
	print(file_list)
	saved_path = os.getcwd()
	print("Current working Directory is "+saved_path)
	os.chdir(r"C:\prank")


	for file_name in file_list:
		randomNum=str(random.randint(1,100))
		print("old name of file -" + file_name)
		print("New name of file -" + randomNum + file_name)
		os.rename(file_name, randomNum + file_name )
	os.chdir(saved_path)

rename_files()

