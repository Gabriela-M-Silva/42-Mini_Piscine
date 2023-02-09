class Intern:
	# to receive parameters (when we create an objects)
	def __init__(self, name = "My name? I’m nobody, an intern, I have no name."):
		self.name = name
	# set the return of class
	def __str__(self):
		return self.name
	# class Coffee in Intern class
	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."
	# work contain raise Exception, that causes a purposeful crash of the program (trated in test function)
	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
	# return result of Coffee class
	def make_coffee(self):
		return self.Coffee()

def test_intern():
	intern1 = Intern() 
	intern2 = Intern('Mark')

	print('Whats your name?')
	print(intern1)
	print('My name is', intern2, '\n')
	print('Coffe hour:')
	print(intern2, 'make coffee...\nResult:', intern2.make_coffee(), '\n')
	print('Work hour:')
	try:
		print(intern1.work())
	except Exception as ex:
		print(ex)

if __name__ == '__main__':
	test_intern()