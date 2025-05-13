class ILOVEPYTHON(object):
	"""docstring for ILOVEPYTHON"""
	def __init__(self):
		self.__someInt = 0
	@property
	def someInt(self):
		return self.__someInt
	@someInt.setter
	def someInt(self, value):
		print("setter called")
		if isinstance(value, int):
			self.__someInt = value

if __name__ == "__main__":
	testVal = ILOVEPYTHON()
	print(testVal._ILOVEPYTHON__someInt)
	print(testVal.someInt)
	testVal.someInt = 5
	print(testVal.someInt)
	testVal.someInt = "vier"
	print(testVal.someInt)
	testVal.__someInt = "vier"
	print(testVal.__someInt)
	print(testVal.someInt)
	testVal.foo = 1.0
	print(testVal.__dict__)
