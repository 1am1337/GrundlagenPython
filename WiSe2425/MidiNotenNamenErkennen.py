import math as math
Kommazahl = [0.083, 0.167, 0.250, 0.333, 0.417, 0.500, 0.583, 0.667, 0.750, 0.833, 0.917, 1.000]			#Kommastellen, wenn man Midizahl durch 12 Teilt		
NotenName = ["C#/Db", "D", "D#/Eb", "E", "F/E#", "F#/Gb", "G", "G#,Ab","A", "B/A#", "H", "C/H#"]			#Notennamen in Anordung von den Kommazahlen
MidiInput = None
while True:
	MidiInput = input("MidiInput: ")
	if MidiInput.isdigit() == True:
		MidiInput = int(MidiInput)
		Verhältnis = MidiInput / 12																			#Verhältnis ist immer Stufe+1 , eine der Kommazahlen
		Ton = round(round(Verhältnis, 3) - math.floor(Verhältnis), 3) 										#Reduziert des Verhältnis auf die Nachkommazahl
		if Ton == 0:																						#Weil x/0 blöd ist
			Ton = 1.000
		for i in range(12):																					#testet welche der Kommazahlen(in der Liste) auf die errechnete Kommazahl zutrifft
			if Ton == Kommazahl[i]:
				print(NotenName[i], math.floor(Verhältnis)-1)												#wenn die Zahlen übereinstimmen wird der entsprechende Notenname und die Stufe ausgegeben
	elif MidiInput == "q":																					#Weil Endlosschleife
		print("Quitting...")
		break
	else: 
		print("Not a MIDI Note")



