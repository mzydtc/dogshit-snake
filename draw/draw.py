#!/usr/bin/env python
#coding=utf-8
import pygame
import sys
from pygame.locals import *
from sys import exit
sys.path.append("..")
from snake.Snake import *
from world.food import *
import random

def start():
    window_width = 800
    window_height = 600

    blockSize = 25

    worldSize = (window_width/blockSize-1,window_height/blockSize-1)

    node_image = 'images/node.png'
    pause_image = 'images/pause.png'
    over_image = 'images/over.jpg'
    meat_image = 'images/meat.png'
    meat_image2 = 'images/meat2.png'
    meat_image3 = 'images/meat3.jpg'
    
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height), 0, 32)
    pygame.display.set_caption("Snake")

    pic = pygame.image.load(node_image).convert_alpha()
    pause_pic = pygame.image.load(pause_image).convert_alpha()
    over_pic = pygame.image.load(over_image).convert_alpha()
    meat_pic = pygame.image.load(meat_image).convert_alpha()
    meat_pic2 = pygame.image.load(meat_image2).convert_alpha()
    meat_pic3 = pygame.image.load(meat_image3).convert_alpha()
    bornPosition = random.randint(10,worldSize[0]-10),random.randint(10,worldSize[1]-10)

    snake = Snake(bornPosition)
    foodObject = food(worldSize)
    alive = True
    def listenKey():
        for event in pygame.event.get(): 
            if event.type == QUIT:
                #接收到退出事件后退出程序
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    return 2
                elif event.key == K_RIGHT:
                    return 3
                elif event.key == K_UP:
                    return 0
                elif event.key == K_DOWN:
                    return 1
                elif event.key == K_SPACE:
                    return 4
                elif event.key == K_RETURN:
                    return 5
                else :
                    return -1
            else :
                return -1
        return -1

    def bangWall(position):
        x = position[0]
        y = position[1]
        if x > worldSize[0] or y > worldSize[1] or x < 0 or y < 0:
            return False
        return True
    meat = meat_pic
    while True:
        screen.fill((200, 200, 200))
        direction = listenKey()
        if direction == 4:
            screen.blit(pause_pic, ((window_width-251)/2, (window_height-140)/2))
            pygame.display.update()
            while True:
                pygame.time.delay(100)
                if listenKey() == 4:
                    break;
        elif direction == 5:
            pass
        else:
            plus = direction+snake.getHead().direction
            if direction != -1 and plus!=1 and plus!=5:
                snake.turn(direction)
        positionList = snake.run()
        if positionList == False or bangWall(positionList[0]) == False:
            screen.fill((255, 255, 255))
            screen.blit(over_pic, ((window_width-580)/2, (window_height-435)/2))
            pygame.display.update()
            while True:
                pygame.time.delay(100)
                if listenKey() == 5:
                    break;
            bornPosition = random.randint(0,worldSize[0]),random.randint(0,worldSize[1])
            snake = Snake(bornPosition)
            foodObject = food(worldSize)
            continue
        for i in positionList:
            screen.blit(pic, (i[0]*blockSize, i[1]*blockSize))
        foodPosition = foodObject.foodPosition
        screen.blit(meat, (foodPosition[0]*blockSize, foodPosition[1]*blockSize))
        pygame.display.update()

        if snake.getHead().position == foodObject.foodPosition:
            snake.eat(foodObject)
            r = random.randint(0,2)
            if r == 0:
                meat = meat_pic
            if r == 0:
                meat = meat_pic2
            else:
                meat = meat_pic3
        pygame.time.delay(100)
