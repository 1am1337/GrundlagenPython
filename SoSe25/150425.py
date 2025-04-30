class midiNote(object):
	"""docstring for midiNote"""
	def __init__(self, pitch, noteDur):
		super(midiNote, self).__init__()
		self.pitch = pitch
		self.noteDur = noteDur
	def octave(self):
		return self.pitch // 12 - 1
	def frequency(self):
		return 440 * 2 ** ((self.pitch - 69) / 12)

class Point(object):
	"""docstring for Point"""
	def __init__(self, xVal: float, yVal: float):
		super(Point, self).__init__()
		if not (isinstance(xVal, float) and isinstance(yVal, float)):
			print("error: wrong type")
		else:
			self.xVal = xVal
			self.yVal = yVal
	def x(self):
		return self.xVal
	def y(self):
		return self.yVal

if __name__ == "__main__":
	# n1 = midiNote(60, 0.25)
	# print(f"octave: {n1.octave()}\nfreq: {n1.frequency()}")
	testCoordinate = Point(10.0, 10.0)
	print(testCoordinate.x(), testCoordinate.y())