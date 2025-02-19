usr_input = input("gebe ein palindrom ein")
if usr_input.lower() == usr_input[::-1].lower():
	print("Super Gemacht")
	print(usr_input.lower())
	break
else:
	print("wrong!")
