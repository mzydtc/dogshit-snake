import random
class food:
	def __init__(self,size):
		self.foodPosition = (0,0)
		self.size = size
		self.freshMeat()
	def freshMeat(self):
		self.foodPosition = (random.randint(0,self.size[0]),random.randint(0,self.size[1]))