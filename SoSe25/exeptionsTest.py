try:
	with open("testFile.txt", "r") as file:
		print(file.read())
except FileNotFoundError:
	print("cant find file :(")
except:
	print("something went wrong :(")


print("hier geht das Programm weiter")