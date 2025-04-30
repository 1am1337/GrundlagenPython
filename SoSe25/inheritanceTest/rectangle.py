import polygon 

class rectangle(polygon.Polygon):
	def __init__(self, base: float, height: float):
		super(rectangle, self).__init__(numPoints=4)
		self.base = base
		self.height = height
	def Area(self) -> float:
		return self.height * self.base

if __name__ == "__main__":
	rect = rectangle(10, 10)
	print(rect.Area())