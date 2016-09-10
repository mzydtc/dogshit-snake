#!/usr/bin/env python
#coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
 
window_width = 800
window_height = 600

node_image = '../images/node.png'
pygame.init()
screen = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption("Hello, World!")
pic = pygame.image.load(mouse_image_filename).convert_alpha()

    direction = listenKey()

    screen.fill((200, 200, 200))
    #计算光标的左上角位置
    screen.blit(pic, (x, y))
    #把光标画上去
    pygame.display.update()

    pygame.time.delay(5)

def listenKey():
    for event in pygame.event.get(): 
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                return 3
            if event.key == K_RIGHT:
                return 4
            if event.key == K_UP:
                return 0
            if event.key == K_DOWN:
                return 1