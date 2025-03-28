import math
import random
noteNames = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
midiRatio = [0.000, 0.083, 0.167, 0.250, 0.333, 0.417, 0.500, 0.583, 0.667, 0.750, 0.833, 0.917]
debugMelody = [71, 71, 69, 67, 72, 72, 71, 69, 74, 71, 67, 74, 74, 76, 72]

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
		for i in range(12):
			if noteMidiMatch == midiRatio[i]:
				noteString = f"{noteNames[i]}{math.floor(ratio-1)}"
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
	scale = [midiInput, midiInput+2, midiInput+4, midiInput+5, midiInput+7, midiInput+9, midiInput+11, midiInput+12]
	return scale
	

def minorScale(midiInput):
	scale = [midiInput, midiInput+2, midiInput+3, midiInput+5, midiInput+7, midiInput+8, midiInput+10, midiInput+12]
	return scale


def blueScale(midiInput):
	scale = [midiInput, midiInput+3, midiInput+5, midiInput+6, midiInput+7, midiInput+10, midiInput+12]
	return scale


def pentaScale(midiInput):
	scale = [midiInput, midiInput+2, midiInput+4, midiInput+7, midiInput+9, midiInput+12]
	return scale


def generateScale(midiInput, scaleType):
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
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
	else:
		return "invalid midi input"

def majTriad(midiInput):
	chord = [midiInput, midiInput+4, midiInput+7]
	return chord

def minTriad(midiInput):
	chord = [midiInput, midiInput+3, midiInput+7]
	return chord

def dom(midiInput):
	chord = [midiInput+7, midiInput+11, midiInput+15]
	return chord

def subDom(midiInput):
	chord = [midiInput+5, midiInput+9, midiInput+12]
	return chord

		
def tristan(midiInput):
	chord = [midiInput+2 , midiInput+6, midiInput+8, midiInput+12]
	return chord


def generateChords(midiInput, chordType):
	if isNum(midiInput) == True:
		midiInput = int(midiInput)
		if chordType == "majTriad":
			return majTriad(midiInput)
		elif chordType == "minTriad":
			return minTriad(midiInput)
		elif chordType == "dom":
			return dom(midiInput)
		elif chordType == "subDom":
			return subDom(midiInput)
		elif chordType == "tristan":
			return tristan(midiInput)
		else:
			return "invalid chordType"
	else:
		return "invalid midi input"


def midiTranspose(midiInput, interval):
	if isNum(midiInput) == True and isNum(interval) == True:
		midiInput = int(midiInput)
		interval = int(interval)
		return midiInput + interval
	else:
		return "invalid Input"

def arpeggio(midiInput, scaleType):
	if isNum(midiInput) == True:
		arp = generateScale(midiInput, scaleType)
		for i in range(3):
			arp.pop(random.randrange(len(arp)))
		return arp


def retrograde(midiMelody):
	midiMelodyRetrograde = midiMelody[::-1]
	return midiMelodyRetrograde


def inverse(midiMelody):
	if type(midiMelody) == list:
		midiMelodyInverse = [midiMelody[0]]
		for i in range(len(midiMelody)-1):
			if isNum(midiMelody[i]) == True:
				midiMelodyInverse.append(midiMelodyInverse[i] - (midiMelody[i+1]- midiMelody[i]))
			else:
				return "invalid Input"
		return midiMelodyInverse
	else:
		return f"wrong format; should be list, is:{type(midiMelody)}"


def invert(midiMelody, invertionType):
	if type(midiMelody) == list:
		if invertionType == "retrograde":
			return retrograde(midiMelody)
		elif invertionType == "inverse":
			return inverse(midiMelody)
		elif invertionType == "retrogradeInversion":
			return retrograde(inverse(midiMelody))
		else:
			return "invalid invertionType"
	else:
		return f"wrong format; should be list, is:{type(midiMelody)}"


def countMidiEvents(midiMelody):
	if type(midiMelody) == list:
		return len(midiMelody)
	else:
		return f"wrong format; should be list, is:{type(midiMelody)}"


def getSubsequentInterval(rootNote, harmonicNote):
	if isNum(rootNote) == True and isNum(harmonicNote) == True:
		return (int(harmonicNote) - int(rootNote))
	else:
		return "invalid Input"


def countIntervals(midiMelody):
	intervals = []
	if type(midiMelody) == list: 
		for i in range(len(midiMelody)-1):
			if isNum(midiMelody[i]) == True:
				intervals.append(midiMelody[i+1] - midiMelody[i])
			else:
				return f"invalid melody component: {midiMelody[i]}"
		return intervals
	else:
		return f"wrong format; should be list, is:{type(midiMelody)}"


def nameToMidi(nameInput):
	if type(nameInput) == str:
		components = list(nameInput)
		if len(components) == 2:
			components.insert(1, " ")
		if components[0].isalpha():
			if components[2].isnumeric():
				midiValue = (int(components[2]) + 1)*12+noteNames.index(components[0])
				if components[1] == "b":
					return midiValue-1
				elif components[1] == "#":
					return midiValue+1
				else:
					return midiValue
		

			else:
				return "invalid Input"
		else:
			return "invalid Input"
	else:
		return "invalid Input"



if __name__ == "__main__":
	print(midiToFreq(60))
	print(freqToMidi(1108.731))
	print(midiToName(69))
	print(getOctave(69))
	print(generateScale(60, "major"))
	print(generateScale(57, "minor"))
	print(generateScale(60, "blue"))
	print(generateScale(60, "penta"))
	print(generateChords(60, "majTriad"))
	print(generateChords(60, "minTriad"))
	print(generateChords(60, "dom"))
	print(generateChords(60, "subDom"))
	print(generateChords(60, "tristan"))
	print(midiTranspose(60, 9))
	print(arpeggio(60, "blue"))
	print(invert(debugMelody, "retrogradeInversion"))
	print(countMidiEvents(debugMelody))
	print(getSubsequentInterval(60, 69))
	print(countIntervals(debugMelody))
	print(nameToMidi("Bb4"))
	pass
