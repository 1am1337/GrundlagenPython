import midiModule as mM 
import sys
sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages")
import pyaudio
import re

splitArgs = r"[ ;,]"
freqList= []
print("Willkommen zur Midi Toolbox!")
print("Bitte geben Sie zunächst mindestens einen Ton ein")
print("Akzeptable Tonnamen sind entweder die Schreibweise A4 (= 440hz) oder die MIDI-Werte: 69 (= A4 = 440hz)")
print("Die verschiedenen Noten sind mit einem Leerzeichen, einem Komma oder Semikolon zu trennen")
print("Um die Toolbox zu verlassen, geben sie \"quit\" ein")
while True:
	tonInputString = input("Ihre Eingabe: \n")
	if tonInputString.strip("") == "quit":
		quit()
	tonInputList = re.split(splitArgs, tonInputString)
	tonInputList[:] = [x for x in tonInputList if x.strip()] #entfernt whitspaces
	for i in range(len(tonInputList)):
		if tonInputList[i].isdigit():
			freqList.append(mM.midiToFreq(tonInputList[i]))
			print(freqList)
		elif tonInputList[i][:-1] in str(mM.noteNames):
			freqList.append(mM.nameToMidi(tonInputList[i]))
			print(freqList)
		else:
			print("Eingabe nicht möglich!")


