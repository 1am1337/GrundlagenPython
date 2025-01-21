note_names = ("C/H#", "C#/Db", "D", "D#/Eb", "E", "F/E#", "F#/Gb", "G", "G#,Ab","A", "B/A#", "H", )

def _getNotenameOktave(midi):
	print(_getNotename(midi), _getOktave(midi))
def _getOktave(midi):
	oktave = int(midi) // 12 -1
	return oktave
def _getNotename(midi):
	noteNameIndex = int(midi) % 12
	noteName = note_names[noteNameIndex]
	return noteName

_getNotenameOktave(int(input("type a midi value: ")))

