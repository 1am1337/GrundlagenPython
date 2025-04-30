class MidiNote():
	noteNames = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
	"""docstring for MidiNote"""
	def __init__(self, pitch: int, duration: float):
		super(MidiNote, self).__init__()
		try:
			self.pitch = int(pitch)
		except:
			print("invalid pitch value")
		try:
			self.duration = float(duration)
		except:
			print("invalid duration value")

	def getPitch(self):
		return self.pitch
	def getNoteName(self):
		return self.noteNames[self.pitch % 12]
	def getOctave(self):
		return self.pitch // 12 - 1
	def getFrequency(self):
		return 440 * 2 ** ((self.pitch - 69) / 12)

if __name__ == "__main__":
	for i in range(128):
		TestNote = MidiNote(i, 0.25)
		print(TestNote.getPitch(), TestNote.getNoteName(), TestNote.getOctave(), TestNote.getFrequency())
		if not i == 127:
			print("------")  #geklaut von adrian :)


		