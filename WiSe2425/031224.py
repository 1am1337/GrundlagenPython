# print("Type 0 to quit")
# mode = int(input("1 for num, 2 for name: "))
# while True:
# 	if mode == 1:
# 		usr_input = input("Enter a whole number: ")
# 		if usr_input == "0":
# 			print("quitting...")
# 			break
# 		elif usr_input.isdigit() == True:
# 			print("Congratulations!!")
# 			break
# 		else:
# 			print("Try again!!")
# 	elif mode == 2:
# 		usr_input = input("Enter a name: ")
# 		if usr_input == "0":
# 			print("quitting...")
# 			break
# 		elif usr_input.isalpha() == True and usr_input.istitle() == True:
# 			print("Congratulations!!")
# 			break
# 		else:
# 			print("Try again!!")
# 	elif mode == 0:
# 		print("quitting...")
# 		break

while True:
	usr_input = input("enter a date in the dd.mm.jjjj format: ")
	if usr_input.replace(".","").isdigit() == True:
		datum = usr_input.split(".", 2)
		if int(datum[0]) <= 31 and int(datum[1]) <= 12:
				print(datum[0],"\n", datum[1],"\n", datum[2], sep="")
				break
		else:
			print("error")
	else:
		print("error")
		continue