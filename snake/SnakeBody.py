from SnakeNode import *
class SnakeBody(SnakeNode):
	def __init__(self,SnakeNode):
		super(SnakeBody,self).__init__(self.last(SnakeNode.position,SnakeNode.direction),SnakeNode.direction)
		position = SnakeNode.position
		direction = SnakeNode.direction

	def last(self,position,direction):
		#up
		if direction == 0:
			return (position[0],position[1]+1)
		#down
		if direction == 1:
			return (position[0],position[1]-1)
		#left
		if direction == 2:
			return (position[0]+1,position[1])
		#right
		if direction == 3:
			return (position[0]-1,position[1])
