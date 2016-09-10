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
		self.bodyList.append(SnakeBody(getTail()))

	def eat(self):
		grow()

	def turn(self,direction):
		self.turnPostition[getHead.position] = direction

	def run(self):
		bodyPosition = []
		for node in bodyList:
			if node.position in self.turnPostition.keys():
				node.turn(self.turnPostition[node.position])
				run()
			bodyPosition.append(node.position)
		return bodyPosition

