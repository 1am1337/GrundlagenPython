usrFileName = input("enter a .txt file name:\n")
if usrFileName != "" and "/" not in usrFileName and "." not in usrFileName:
	try:
		with open(f"{usrFileName}.txt", "r") as file:
			print(f"\nfile contains:\n{file.read()}\n")
	except FileNotFoundError:
		fileCreationInput = input((f"file doesnt exist\ndo you want to create {usrFileName}.txt? (y/n)\n"))
		if isinstance(fileCreationInput, str):
			if fileCreationInput == "y":
				with open(f"{usrFileName}.txt", "w") as file:
					file.write("")
					print("file created :)")
			elif fileCreationInput == "n":
				print("file not created\nquitting...")
				quit()
	except IOError:
		print("IOError\nquitting...")
		quit()
	except ValueError:
		print("ValueError\nquitting...")
		quit()
	usrNewContentPrompt = input("do you want to add new content to the file? (y/n)\n")
	if isinstance(usrNewContentPrompt, str) and usrNewContentPrompt == "y":
		usrNewFileContent = str(input("enter new file content:\n"))
		if usrNewFileContent != "":
			with open(f"{usrFileName}.txt", "a") as file:
				file.write(f"\n{usrNewFileContent}")
		else:
			print("cant be empty!\nquitting...")
			quit()
	elif isinstance(usrNewContentPrompt, str) and usrNewContentPrompt == "n":
		print("did not want to enter new content.\nquitting...")
		quit()

else:
	print("invalid input")

