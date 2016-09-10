class SnakeNode(object):

	def __init__(self,position,direction):
		self.position = position
		self.direction = direction
		self.next()

	def turn(self,direction):
		self.direction = direction
		self.next()

	def next(self):
		#up
		if self.direction == 0:
			self.nextPosition = (self.position[0],self.position[1]-1)
		#down
		if self.direction == 1:
			self.nextPosition = (self.position[0],self.position[1]+1)
		#left
		if self.direction == 2:
			self.nextPosition = (self.position[0]-1,self.position[1])
		#right
		if self.direction == 3:
			self.nextPosition = (self.position[0]+1,self.position[1])

	def run(self):
		self.position = self.nextPosition
		self.next()