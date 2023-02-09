import random
from  beverages import *

class CoffeeMachine:
	def __init__(self):
		self.count = 0
	class EmptyCup(HotBeverage):
		def __init__(self, name = "empty cup", price = 0.90):
			super().__init__(name, price)
		def description(self):
			return "An empty cup?! Gimme my money back!"
	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")
	def repair(self):
		self.count = 0
	def serve(self, drink):
		if isinstance(drink(), HotBeverage) == False:
			raise Exception("We don't have that on the drinks list")
		if self.count == 10:
			return CoffeeMachine.BrokenMachineException()
		else:
			self.count += 1
			list_drink = [drink(), CoffeeMachine.EmptyCup()]
			sended_drink = random.choice(list_drink)
			print(self.count)
			return sended_drink

def machine():
	machine = CoffeeMachine()
	random_drink = random.choice([Coffee, Tea, Chocolate, Cappuccino])

	i = 0
	count = 1
	while (i <= 21): #break AFTER serving 10 drinks
		try:
			print(machine.serve(random_drink), '\n')
		except Exception as ex:
			print(ex)
		if count % 11 == 0: #repair machine
			machine.repair()
			print('Machine repaired.', '\n')
		i += 1
		count += 1

if __name__ == '__main__':
	machine()
