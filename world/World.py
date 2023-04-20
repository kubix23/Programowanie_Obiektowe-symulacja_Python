import os
import pickle
import time

import pygame

from organisms.Human import Human
from view.WindowGame import WindowGame
from view.WorldPanel import WorldPanel
from view.EventList import EventList

class World:
    def __init__(self, sizeX, sizeY, hex):
        self.worldPanel = None
        self.__save = None
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__map = []
        self.__organisms = []
        self.__hex = hex
        for j in range(0, sizeY * sizeX):
            self.__map.append(None)
        self.insertOrganism(Human(0, 0, self))
        EventList.add(self)

    @classmethod
    def assign(cls, old):
        return cls(old.__sizeX, old.__sizeY, old.__hex)

    def setWorldPanel(self, worldPanel):
        self.worldPanel = worldPanel

    def save(self):
        temp = self.worldPanel
        file = open('save.dat', 'wb')
        self.worldPanel = None
        file.write(pickle.dumps(self))
        self.worldPanel = temp
        file.close()

    def load(self):
        file = open('save.dat', 'rb')
        dataPickle = file.read()
        world = pickle.loads(dataPickle)
        EventList.add(world)
        for a in world.getOrganisms():
            if isinstance(a, Human):
                EventList.add(a)
        WindowGame(world)

    def isHex(self):
        return self.__hex

    def setOrganisms(self, organisms):
        self.__organisms = organisms

    def getSizeX(self):
        return self.__sizeX

    def getSizeY(self):
        return self.__sizeY

    def getOrganismsSize(self):
        return len(self.__organisms)

    def getOrganism(self, i):
        return self.__organisms[i]

    def getCell(self, x, y):
        a = y * self.__sizeX + x
        return self.__map[int(a)]

    def getWorldPanel(self):
        return self.__worldPanel

    def setCell(self, x, y, organism):
        self.__map[int(y * self.__sizeX + x)] = organism

    def takeTurn(self):
        for o in self.__organisms:
            o.yearOlder(1)
            o.action()
        self.updateWorld()

    def insertOrganism(self, organism):
        if self.getCell(organism.getPosX(), organism.getPosY()) == None:
            i = 0
            for o in self.__organisms:
                if organism.getInitiation() > o.getInitiation():
                    break

                if organism.getInitiation() == o.getInitiation() and organism.getAge() > o.getAge():
                    break
                i = i + 1
            self.__organisms.insert(i, organism)
            self.setCell(organism.getPosX(), organism.getPosY(), organism)
            organism.setWorld(self)

    def getOrganisms(self):
        return self.__organisms

    def removeOrganism(self, organism):
        self.setCell(organism.getPosX(), organism.getPosY(), None)
        self.__organisms.remove(organism)

    def updateWorld(self):
        for i in range(0,self.__sizeY):
            for j in range(0,self.__sizeX):
                self.worldPanel.updatePoint(j, i, None)

        for o in self.__organisms:
            self.worldPanel.updatePoint(o.getPosX(), o.getPosY(), o.getSymbol())

    def event(self, event):
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
                self.takeTurn()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_o]:
                self.save()
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_l]:
                self.load()
