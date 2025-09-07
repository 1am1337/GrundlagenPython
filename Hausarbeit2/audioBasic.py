import numpy as np
import matplotlib.pyplot as plt
import wavio


sr = 96000 							#sampling rate in Hz
length = 0.5 						#in seconds
pauseDur = 0.01
freqTable1 = [1209, 1336, 1477] 	#in Hz
freqTable2 = [697, 770, 852, 941] 	#in Hz
usrInput = "04915734426415" 		#placeholder (call me ;)
usrInputList = []					#list of the seperated usrInput-Values
freqTableCombined = []				#Combination of freqTable1 and freqTable2, stored as tuplets in a list
usrFreqList =[]						#list of tuples derived from freqTableCombined and usrInputList
individualY = None					#y-Value of an individual usrInput tuple
totalY = np.array([])				#numpy array for storing all individualY's


freqTableCombined.append((freqTable1[1], freqTable2[3])) 	#equal to 0 on the "numpad", would annoying to add with the others
for i in range(3):											#adds the frequencies of 1-9
	for j in range(3):
		freqTableCombined.append((freqTable1[j], freqTable2[i]))


while True:													#user input handler
	usrInput = input("Enter a Telephone Number: ")
	if usrInput.isnumeric() == True :
		usrInput = usrInput.replace(" ", "")  				#Removes all spaces 
		for i in range(len(usrInput)):
			usrInputList.append(int(usrInput[i:i+1]))
		break
	elif usrInput.lower() == "quit":
		quit()
	else:
		print("invalid Input, try again(enter quit to quit)")

for i in range(len(usrInput)):														#list of tuples derived from freqTableCombined and usrInputList
	usrFreqList.append(freqTableCombined[int(usrInput[i])])

soundDur = np.linspace(0, length, num=int(sr * length))								#creates an numpy array with the lenght of a single digit

soundDurWithPause = (length * len(usrInput)) + (pauseDur * (len(usrInput)))   		#calculates the length of a single sound + length of the pause between sounds

pause = np.linspace(0, pauseDur, num=int(sr * pauseDur))							#creates an numpy array with the length of a single pause

totalTime = np.linspace(0, soundDurWithPause, num=int(sr * soundDurWithPause))		#calulates the total length of all sounds and all pauses

for i in range(len(usrInput)):														
	individualY = (np.sin(2 * np.pi * soundDur * usrFreqList[i][0]))				#fills the y values corresponding to the first of two frequencies
	individualY = individualY + (np.sin(2 * np.pi * soundDur * usrFreqList[i][1]))	#adds the second frequency
	individualY = np.concatenate((individualY, pause))								#"appends" the pause 
	totalY = np.concatenate((totalY, individualY))									#adds the sound to the total "collection" of sounds


totalY = totalY / np.max(np.abs(totalY))											#normalisation				

wavio.write("phone.wav", totalY, sr, sampwidth=3)									#writes the file
print("file stored under 'phone.wav'")

