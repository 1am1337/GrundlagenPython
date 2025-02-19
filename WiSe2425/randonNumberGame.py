	import random as r 																									#dann muss ich nicht immer random ausschreiben
usr_input = None																									#input/variablen vor der while schleife initiieren
usr_continue = None																										
counter = 0
random_number = r.randint(1, 100)
#print(random_number)																								#die nummer fürs testen ausgeben
print("Eine zufällige Nummer von 1 bis 100 wurde generiert. Welche wohl?\nGebe 0 ein um das Spiel zu beenden")
while True:
	usr_input = input("Gebe eine Nummer von 1 bis 100 ein: ")
	counter += 1
	if usr_input.isdigit() == True:																					#Testen ob der Input eine Zahl ist
		usr_input = int(usr_input)
		if usr_input == random_number:																				#testen ob die nummer erraten wurde
			print("Du hast die Zahl in", counter,"Versuchen erraten! :)\a")											#erfolgsmeldung + anzahl von versuchen
			usr_continue = input("Möchtest du weiter spielen? (Y/N):")												#Option für neustart anbieten
			if usr_continue.lower() == "y":
				random_number = r.randint(1, 100)																	#variablen zurücksetzen
				counter = 0
				#print(random_number)																				#die nummer fürs testen ausgeben
			if usr_continue.lower() == "n":
				print("Beendet das Programm...")
				break
		elif usr_input == 0:																						#wenn input null ist programm beenden
			print("Beendet das Programm...")
			break
		elif usr_input < random_number:																				#ist der input zu klein?
			print("Deine Zahl ist zu klein!")
		elif usr_input > random_number:																				#ist der input zu groß?
			print("Deine Zahl ist zu groß!")
	else:
		print("Keine Zahl!")