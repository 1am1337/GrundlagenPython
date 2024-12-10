usr_list = []											#initiert die liste und den user input 
usr_input = None
print("Um die Eingabe zu beenden, exit eingeben")		#sonst weiß der user nicht wie man die Endloschleife beendet
print("Um Element entfernen das Element mit / neueingeben")
print("showlist schreiben um die liste auszugeben")

while True:
	usr_input = input("Neues Element hinzufügen:")		#der input typ ist letztendlich egal, wenn gewollt, könnte man alles zur zahl oder zum string machen, um spezifische sortierungsmethoden anwenden zu können	
	if usr_input.lower() == "exit":						#breakout condition
		usr_list.sort(key=len, reverse = True)			#sortiert die liste nach der länge vom input, anfangend beim längsten element
		print(usr_list)  								#gibt die sortierte liste aus
		break											#beendet die endlosschleife
	elif usr_input.startswith("/") == True:				#wenn mit / beginnt
		usr_input = usr_input.lstrip("/")				#"/" entfernen 
		usr_list.pop(usr_list.index(usr_input))			#element aus der liste entfernen
	elif usr_input.lower() == "showlist":				#falls input showlist ist
		print(usr_list)									#liste ausgeben
	else:
		usr_list.append(usr_input)						#fügt den user input der liste hinzu
