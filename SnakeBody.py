import SnakeHead
import SnakeNode
class SnakeBody:
	def __init__(self):
		bodyList=[]
		bodyList.add(SnakeHead.newHead())
		
	def getTail():
		return bodyList[-1]
	
	def grow():
		bodyList.append(SnakeNode.newNode())