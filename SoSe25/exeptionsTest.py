try:
	
	with open("wringFile.txt", "r"):
		print(file.read())
except FileNotFoundError:
	print("cant find file :(")
except:
	print("something went wrong :c")


print("hier geht das Programm weiter")