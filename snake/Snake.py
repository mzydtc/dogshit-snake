from SnakeHead import *
from SnakeBody import *
import random
class Snake():
	def __init__(self,position):
		direction = random.randint(0,3)
		self.bodyList=[]
		self.turnPostition={}
		self.bodyList.append(SnakeHead(position,direction))
		
	def getTail(self):
		return self.bodyList[-1]
	
	def getHead(self):
		return self.bodyList[0]

	def grow(self):
		self.bodyList.append(SnakeBody(self.getTail()))

	def eat(self,food):
		self.grow()
		food.freshMeat()

	def turn(self,direction):
		self.turnPostition[self.getHead().position] = direction

	def run(self):
		bodyPosition = []
		for node in self.bodyList:
			if node.position in self.turnPostition.keys():
				node.turn(self.turnPostition[node.position])
				if node is self.getTail():
					self.turnPostition.pop(node.position)
			node.run()
			bodyPosition.append(node.position)
		if bodyPosition.count(self.getHead().position) > 1:
			return False
		return bodyPosition