class Polygon():
	def __init__(self, numPoints: int):
		self.numPoints = numPoints
	def returnNumPoints(self):
		return self.numPoints
	def innerAngleSum(self):
		return (self.numPoints - 2) * 180

if __name__ == "__main__":
	poly = Polygon(3)
	print(poly.innerAngleSum())
		