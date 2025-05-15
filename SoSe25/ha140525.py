class validInput(Exception):
		"""docstring for validInput"""
		def __init__(self, arg):
			self.arg = arg
				
usrFileName = input("enter a .txt file name: ")
if usrFileName != "" and "/" not in usrFileName and "." not in usrFileName:
	try:
		with open(f"{usrFileName}.txt", "r") as file:
			print(file.read())
	except FileNotFoundError:
		fileCreationInput =input((f"file doesnt exist\ndo you want to create {usrFileName}.txt?\t(y/n)\n"))
else:
	print("invalid input")

