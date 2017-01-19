class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name=last_name
		self.eye_color=eye_color

	def show_info(self):
		print("Last Name "+self.last_name)
		print("Eye Color "+self.eye_color)

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
	def show_info(self):
		print("number of toys - "+str(self.number_of_toys))

#dipti_adekoya = Parent ("adekoya", "brown")
#print(dipti_adekoya.last_name)

funi_adekoya = Child("adekoya","green","6")
funi_adekoya.show_info()
#print(funi_adekoya.last_name)
#print(funi_adekoya.number_of_toys)