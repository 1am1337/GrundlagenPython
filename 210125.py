note_names = ("C/H#", "C#/Db", "D", "D#/Eb", "E", "F/E#", "F#/Gb", "G", "G#,Ab","A", "B/A#", "H", )

def _getNotenameOctave(midi):
	print(_getNotename(midi), _getOctave(midi))

def _getOctave(midi):
	octave = int(midi) // 12 -1
	return octave

def _getNotename(midi):
	noteNameIndex = int(midi) % 12
	noteName = note_names[noteNameIndex]
	return noteName

_getNotenameOctave(int(input("type a midi value: ")))

