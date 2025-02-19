import random
random_number = random.randint(1,100)
anzahl_versuche = 0 	

while True:
	input_str = input("Input: ")
	input_str = input_str.strip(" ").strip("\t")
	input_int = int(input_str)
	anzahl_versuche += 1
	if input_int == 0:
		print("Exit", anzahl_versuche-1)
		break
	if input_int < random_number:
		print("<")
		continue
	if input_int > random_number:
		print(">")
		continue
	print("{} Versuche".format(anzahl_versuche))
	break	