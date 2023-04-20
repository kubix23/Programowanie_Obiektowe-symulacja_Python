import json
import math
import pickle
from json import JSONEncoder

import pygame

from organisms.Human import Human
from view.Control import Control
from view.EventList import EventList
from view.Point import Point


class WorldPanel:
    def __init__(self, world, hex):
        self.__screen = pygame.display.set_mode((700, 800))
        self.__group = pygame.sprite.LayeredUpdates()
        self.__width = self.__screen.get_width()
        self.__height = self.__screen.get_height() - 100
        self.__sizeX = world.getSizeX()
        self.__sizeY = world.getSizeY()
        self.__popup = pygame.rect.Rect(0, 0, 0, 0)
        self.__panel = []
        self.__hex = hex
        if hex:
            self.__number = 6
        else:
            self.__number = 4
        world.worldPanel = self
        self.drawGrid(world)
        Control(0, self.__height, world,  self.__group)
        world.updateWorld()
        run = True
        while run:

            for event in pygame.event.get():
                EventList.checkEvent(event)
                if event.type == pygame.QUIT:
                    run = False
            self.__screen.fill((0,0,0))
            self.__group.update()
            self.__group.draw(self.__screen)
            pygame.display.flip()

    def generatePath(self, number):
        polygon = []
        centerX = (self.__width/self.__sizeX) / 2
        centerY = (self.__height/self.__sizeY) / 2
        angleOfset = 180 / number if number % 2 == 0 else 90
        for i in range(0, number):
            angleDegrees = ((360 / number) * i) + angleOfset
            angleRad = math.radians(angleDegrees)
            x = centerX + centerX * math.cos(angleRad)
            y = centerY + centerY * math.sin(angleRad)
            polygon.append((x, y))
        return polygon

    def drawGrid(self, world):
        rowHeight = self.__height / self.__sizeY
        colWidth = self.__width / self.__sizeX
        path = self.generatePath(self.__number)
        yPos = 0
        for row in range(0,self.__sizeY):
            offset = 0
            colCount = self.__sizeX
            if row % 2 == 0 and self.__number == 6:
                offset = colWidth / 2
            xPos = offset
            for col in range(0, colCount):
                self.__panel.append(Point(self, self.__group, 0, xPos, yPos, colWidth, rowHeight, world, path,col,row))
                xPos += colWidth;
            yPos += rowHeight * 0.75 if self.__number == 6 else rowHeight;
            if self.__number == 6:
                pygame.display.set_mode((735, 800))

    def getShape(self, x, y):
        return self.__panel[int(y * self.__sizeX + x)]

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def setPopup(self, popup):
        self.__popup = popup

    def getPopup(self):
        return self.__popup

    def updatePoint(self, x, y, text):
        self.getShape(x, y).setName(text)
