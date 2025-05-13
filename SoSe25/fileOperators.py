try:
	file = open("testFile.txt", "r")
except IOError:
	print("couldn't load file")
except ArithmeticError:
	print("math is wrong")
except ValueError:
	print("cant convert type")
except FileNotFoundError:
	print("file location invalid")
except IndexError:
	print("index out of range")
except (RuntimeError, TypeError):
	print("smth went terribly wrong")
	print("cant read dict")
else:
	print("file loaded!")
finally:
	file.close()


