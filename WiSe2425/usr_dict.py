usr_dict = {}
usr_input = None
print("Gebe nichts ein um die Eingabe zu beenden.")
while True:
	usr_input = input("Gebe ein String ein: ").lower()
	if usr_input in usr_dict:
		usr_dict[usr_input] += 1
	elif usr_input == "":
		for items in usr_dict.items():
			print(str(items).replace(",", ":")[1:-1])
		break
	else:
		usr_dict[usr_input] = 1

