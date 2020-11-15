from  sys import argv

script, name, = argv

class NameTag:
	def __init__(self, myname):
		self.myname = myname
	
	def say(self):
		print(f'Hello, my name is {self.myname}')

NameTag(str(name)).say()

