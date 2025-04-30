class MidiEvent():
	def __init__(self, dur):
		self.dur = dur
	def getDuration(self):
		try:
			return float(self.dur)
		except:
			print("invalid duration")

class MidiNote(MidiEvent):
	noteNames = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
	def __init__(self, pitch: int, dur: float):
		super(MidiNote, self).__init__(dur)
		try:
			self.pitch = int(pitch)
		except:
			print("invalid pitch value")
	def getPitch(self):
		return self.pitch
	def getNoteName(self):
		return self.noteNames[self.pitch % 12]
	def getOctave(self):
		return self.pitch // 12 - 1
	def getFrequency(self):
		return 440 * 2 ** ((self.pitch - 69) / 12)

class MidiRest(MidiEvent):
	def __init__(self, dur: float):
		super(MidiRest, self).__init__(dur)
	def getLabel(self):
		try:
			return float(self.dur)
		except:
			print("invalid duration")
debugMelody = [71, 71, 69, 67, 72, 72, 71, 69, 74, 71, 67, 74, 74, 76, 72]

if __name__ == "__main__":
	events = [
		MidiNote(71, 0.25),
		MidiNote(71, 0.25),
		MidiNote(69, 0.25),
		MidiNote(67, 0.25),
		MidiRest(0.0625),
		MidiNote(72, 0.25),
		MidiNote(72, 0.25),
		MidiNote(71, 0.25),
		MidiNote(69, 0.25),
		MidiNote(74, 0.25),
		MidiNote(71, 0.25),
		MidiNote(67, 0.25),
		MidiNote(74, 0.25),
		MidiNote(74, 0.375),
		MidiRest(0.0625),
		MidiNote(76, 0.125),
		MidiNote(72, 0.5)
	]
	for i in events:
		if isinstance(i, MidiNote):
			print(f"{i.getNoteName()}{i.getOctave()}: {i.getDuration()}s")
		elif isinstance(i, MidiRest):
			print(f"Rest: {i.getLabel()}s")

	
		