class car(object):
	"""docstring for car"""
	def __init__(self, brand: str, model: str):
		super(car, self).__init__()
		self.brand = brand
		self.model = model
	def showDetails(self):
		print(f"{self.brand}")

class eletricCar(car):
	"""docstring for eletricCar"""
	def __init__(self, brand, model, battery):
		super(eletricCar, self).__init__(brand, model)
		self.battery = battery
	def showDetails(self):
		super().showDetails()
		print(f"{self.battery}")

my_car = car("toyota", "corolla")
my_car.showDetails()
print("")
my_eletricCar = eletricCar("Audi", "S", 90)
my_eletricCar.showDetails()
		