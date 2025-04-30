class Point2D(object):
	"""docstring for Point2D"""
	def __init__(self, xPos: float, yPos: float):
		try:
			self.xPos = float(xPos)
		except:
			print("error")
		try:
			self.yPos = float(yPos)
		except:
			print("error")
	def addPoints(self, pointToBeAdded):
		self.xPos = self.xPos + pointToBeAdded.xPos
		self.yPos = self.yPos + pointToBeAdded.yPos
	def addedPoint(self, pointToBeAdded):
		point2D = Point2D(self.xPos + pointToBeAdded.xPos, self.yPos + pointToBeAdded.yPos)
		return point2D



if __name__ == "__main__":
	point_0 = Point2D(4, 20)
	point_1 = Point2D(6, 9)
	point_0.addedPoints(point_1)
	print(point_0.xPos)
