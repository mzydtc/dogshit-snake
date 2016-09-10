#!/usr/bin/env python
from snake.Snake import *
from snake.SnakeNode import *
if __name__=='__main__':
	a=Snake()
	print a.bodyList
	print a.getHead().getPosition()