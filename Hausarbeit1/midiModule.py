import math
noteNames = ["C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B", "C"]
midiRatio = [0.083, 0.167, 0.250, 0.333, 0.417, 0.500, 0.583, 0.667, 0.750, 0.833, 0.917, 1.000]

def isNum(testInput):
	try:
		float(testInput)
		return True
	except ValueError:
		return False
		

def midiToFreq(midiInput):
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
		freq = round(440 * math.pow(2, (midiInput - 69)/12), 3)
		if midiInput <= 20:
			return f"entered value under the lowest possible value; would be {freq}hz"
		else:
			return freq
	else:
		return "invalid Input; try a number"


def freqToMidi(freqInput):
	freqList = []
	if isNum(freqInput) == True:
		freqInput = float(freqInput)
		for i in range(21, 128):
			freqList.append(round(midiToFreq(i), 3))
		try:
			freqList.index(freqInput)
			return freqList.index(freqInput)
		except ValueError:
			return "invalid input; cant match freq to midi; try a number with 3.000 decimal places"
	else:
		return "invalid Input; try a number"	


def midiToName(midiInput):
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
		ratio = midiInput / 12
		noteMidiMatch = round(round(ratio, 3) - math.floor(ratio), 3)
		if noteMidiMatch == 0.000:
			noteMidiMatch == 1.000
		for i in range(12):
			if noteMidiMatch == midiRatio[i]:
				noteString = f"{noteNames[i]} {math.floor(ratio-1)}"
				return noteString
	else:
		return "invalid Input; try a number"	


def getOctave(midiInput):
	if isNum(midiInput) == True:
		midiInput = int(midiInput) / 12
		return math.floor(midiInput -1)
	else:
		return "invalid Input; try a number"


def majorScale(midiInput):
	scale = []
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
		scale = midiInput, midiInput+2, midiInput+4, midiInput+5, midiInput+7, midiInput+9, midiInput+11, midiInput+12
		return scale
	else:
		return "invalid Input"
	

def minorScale(midiInput):
	scale = []
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
		scale = midiInput, midiInput+2, midiInput+3, midiInput+5, midiInput+7, midiInput+8, midiInput+10, midiInput+12
		return scale
	else:
		return "invalid Input"


def blueScale(midiInput):
	scale = []
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
		scale = midiInput, midiInput+3, midiInput+5, midiInput+6, midiInput+7, midiInput+10, midiInput+12
		return scale
	else:
		return "invalid Input"	


def pentaScale(midiInput):
	scale = []
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
		scale = midiInput, midiInput+2, midiInput+4, midiInput+7, midiInput+9, midiInput+12
		return scale
	else:
		return "invalid Input"	


def generateScale(midiInput, scaleType):
	if scaleType == "major":
		return majorScale(midiInput)
	elif scaleType == "minor":
		return minorScale(midiInput)
	elif scaleType == "blue":
		return blueScale(midiInput)
	elif scaleType == "penta":
		return pentaScale(midiInput)
	else:
		return "invalid scaleType"



if __name__ == "__main__":
	print(midiToFreq(85))
	print(freqToMidi(1108.731))
	print(midiToName(85))
	print(getOctave(85))
	print(generateScale(60, "major"))
	print(generateScale(57, "minor"))
	print(generateScale(60, "blue"))
	print(generateScale(60, "penta"))
