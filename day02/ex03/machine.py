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
		print('Machine repared') ####tem q printar dps de arrumar?
	def serve(self, drink):
		if isinstance(drink(), HotBeverage) == False:
			raise Exception("We don't have that on the drinks list")
		if self.count == 10:
			print(CoffeeMachine.BrokenMachineException()) #printa q quebrou
			return 
		else:
			self.count += 1
			list_drink = [drink(), CoffeeMachine.EmptyCup()]
			sended_drink = random.choice(list_drink)
			#print(self.count) #serve random drink
			return sended_drink
		
def machine():
	tr = CoffeeMachine() #p teste -- isso vai estar no serve()
	var_random = random.choice([Coffee, Tea, Chocolate, Cappuccino]) #tem hotbeverage?

#	print(tr.EmptyCup())
	i = 0
	while (i <= 21): #break AFTER serving 10 drinks
		try:
			print(tr.serve(var_random), '\n')  #ta enviando None em algum momento
		except Exception as ex:
			print(ex)
		if i % 10 == 0: #errado
			tr.repair()
		i += 1

if __name__ == '__main__':
	machine()
