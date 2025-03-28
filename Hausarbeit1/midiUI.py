import midiModule as mM 
import sys
sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages")
from pysine import sine
import re

splitArgs = r"[ ;,]"
userMode = "noteInput"
freqList = []
durList = []
print("Willkommen zur Midi Toolbox!")
print("Bitte geben Sie zunächst mindestens einen Ton ein")
print("Akzeptable Tonnamen sind entweder die Schreibweise A4 (= 440hz) oder die MIDI-Werte: 69 (= A4 = 440hz)")
print("Die verschiedenen Noten sind mit einem Leerzeichen, einem Komma oder Semikolon zu trennen")
print("Um die Toolbox zu verlassen, geben sie \"quit\" ein")
while True:
	while userMode == "noteInput":
		tonInputString = input("\nUm die Notenwerteingabe zu beenden, geben sie \"next\" ein \nIhre Eingabe: \n")
		if tonInputString.strip("") == "quit":
			quit()
		elif tonInputString.strip("") == "next":
			userMode = "durInput"
		tonInputList = re.split(splitArgs, tonInputString)
		tonInputList[:] = [x for x in tonInputList if x.strip()] #entfernt whitspaces
		if all(x.isdigit() for x in tonInputList):
			for i in range(len(tonInputList)):
				freqList.append(mM.midiToFreq(tonInputList[i]))
		elif all(str(x)[:-1] in str(mM.noteNames) for x in tonInputList):
			for i in range(len(tonInputList)):
				freqList.append(mM.midiToFreq(mM.nameToMidi(tonInputList[i])))
		else:
			if tonInputString.strip("") == "quit":
				quit()
			elif tonInputString.strip("") == "next":
				userMode = "durInput"
			else:
				print("error:", tonInputList, type(tonInputList), type(tonInputList[0]), userMode)


	while userMode == "durInput":
		if len(freqList) > 0:
			print("\nBitte geben Sie die entsprechenden Tonlängen ein. Im Format 4 = viertel, 8 = achtel, 1 = ganze, usw.")
			print("\nUm die Tonlängeneingabe zu beenden geben Sie \"next\" ein")
			durInputStr = input("Ihre Eingabe: ")
			durInputList = re.split(splitArgs, durInputStr)
			durInputList[:] = [x for x in durInputList if x.strip()]
			if all(x.isdigit() for x in durInputList) and len(freqList) == len(durInputList):
				for i in range(len(durInputList)):
					durList.append(4 / int(durInputList[i]))
				print(durList)
			else:
				if durInputStr.strip("") == "quit":
					quit()
				elif durInputStr.strip("") == "next":
					userMode = "exportInput"
				else:
					print("error:", durInputList, type(durInputList), type(durInputList[0]), len(durInputList), userMode)
		else:
			print("Sie haben noch keine Töne eigegeben!")
			userMode = "noteInput"

	while userMode == "exportInput":
		print("\n Sie haben ihre Melodie erfoleich eingeben")
		print(freqList, "\n", durList)
		bpm = input("Geben Sie die BPM an: ")
		if bpm.isdigit():
			for i in range(len(durList)):
				freq = freqList[i]
				dur = (60/int(bpm)) * durList[i]
				sine(frequency = freq, duration = dur)
		elif bpm == "quit":
			quit()
			

