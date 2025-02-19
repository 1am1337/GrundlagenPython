#Schreibt ein Python, das vom User die Eingabe einer MIDI-Tonhöhe verlangt
#Danach sollen die MIDI-Tonhöhen ausgegeben werden, die zusammen mit der Eingabe als Grundton, einen Dur-Dreiklang ergeben
#Ist C4 höher als alle Noten dieses Dreiklangs? (Ausgabe als Boolean)
#MIDI geht von C -2 = 0 bis G8 = 127 -> MIDI +1 = Halbtonschritt

print("Type quit or q to exit program")							
MIDI_Note = None															#ermöglicht den input erst innerhalb der schleife zu fragen
while True:
	MIDI_Note = input("Gebe eine MIDI Tonhöhe ein: ")
	if MIDI_Note.isdigit() == True:											#testet ob input eine zahl ist
		MIDI_Note = int(MIDI_Note)											#wenn ja konvertiert input zur zahl
		if MIDI_Note >= 0 and MIDI_Note <= 127:								#testet ob die zahl innerhalb des midi bereiches ist
			print("Dreiklang: ", MIDI_Note, MIDI_Note +3, MIDI_Note +7)		#Wenn ja, kann der dur dreiklang ausgegeben werden
			print("Der Akkord ist höher als C4?:", MIDI_Note+7 > 60)		#gibt aus ob der dreiklang höher(True) oder niedriger(False) ist
		else:
			print("Note außerhalb des MIDI Bereichs")						#fehlermeldung, falls die eingabe außerhalb von dem MIDI bereich ist
	elif MIDI_Note == "quit" or "q":										#weil sonst eine endlosschleife entsteht
		print("Quitting...")
		break 		
	else:
		print("Keine MIDI Note")											#fehlermeldung, falls die eingabe außerhalb von dem MIDI bereich ist
		

