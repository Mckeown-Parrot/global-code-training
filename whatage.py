studentList = ["james", "kwaku", "kelvin"]
ageList = {}

def whatAge():
	for i in studentList:
		ageInput = input(f"Hello {i} , what is your age ? ")
		ageList[i]=ageInput
	print(ageList)
		
		
whatAge()
