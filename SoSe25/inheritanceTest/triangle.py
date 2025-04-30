import polygon

class triangle(polygon.Polygon):
	def __init__(self, base: float, height: float):
		super(triangle, self).__init__(numPoints=3)
		self.base = base
		self.height = height
	def Area(self) -> float:
		return (self.height*self.base)/2

if __name__ == "__main__":
	tri = triangle(10, 10)
	print(tri.Area())