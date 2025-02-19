# anfangspunkt = int(input("Anfangspunkt: "))
# reichweite = int(input("Bis welche Zahl möchtest du alle geraden erfahren?: "))
# for i in range(anfangspunkt ,reichweite):
# 	if i % 2 == 0:
# 		print(i)

# Note = None
# Namenname = ["Sehr gut", "Gut", "Befriedigend", "Ausreichend", "Mangelhaft", "Ungenügend"]
# while True:
# 	Note = int(input("Note: "))
# 	if Note >= 1 and Note <= 6: 
# 		print(Namenname[Note-1])
# 	elif Note == 404:
# 		print("Quitting...")
# 		break
# 	else:
# 		print("keine Note")

def MultFunc(usr_input,usr_mult):
	usr_input = usr_input * usr_mult
	return(usr_input)

Faktor1 = float(input("Faktor 1: "))
Faktor2 = float(input("Faktor 2: "))
print(MultFunc(Faktor1, Faktor2))



