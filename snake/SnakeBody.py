from SnakeNode import *
class SnakeBody(SnakeNode):
	def __init__(self,SnakeNode):
		super(SnakeHead,self).__init__(last(SnakeNode.position,SnakeNode.direction),SnakeNode.direction)
		position = SnakeNode.position
		direction = SnakeNode.direction

	def last(position,direction):
		#up
		if direction = '0':
			return (position[0],position[1]+1)
		#down
		if direction = '1':
			return (position[0],position[1]-1)
		#left
		if direction = '3':
			return (position[0]+1,position[1])
		#right
		if direction = '4':
			return (position[0]-1,position[1])
