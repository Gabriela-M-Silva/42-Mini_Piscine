class HotBeverage:
	def __init__(self, name = "hot beverage", price = 0.30):
		self.price = price
		self.name = name
	def description(self):
		return "Just some hot water in a cup."
	def __str__(self):
		return 'name : ' + self.name + '\nprice : ' + format(self.price,'.2f') + '\ndescription : ' + self.description()

class Coffee(HotBeverage):
	def __init__(self, name = "coffee", price = 0.40):
		super().__init__(name, price)
	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self, name = "tea"):
		super().__init__(name)

class Chocolate(HotBeverage):
	def __init__(self, name = "chocolate", price = 0.50):
		super().__init__(name, price)
	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self, name = "cappuccino", price = 0.45):
		super().__init__(name, price)
	def description(self):
		return "Un po’ di Italia nella sua tazza!"

def	test_beverages():
	print(HotBeverage(), '\n')
	print(Coffee(), '\n')
	print(Tea(), '\n')
	print(Chocolate(), '\n')
	print(Cappuccino())

if	__name__ == '__main__':
	test_beverages()