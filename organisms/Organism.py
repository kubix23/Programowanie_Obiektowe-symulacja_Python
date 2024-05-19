import math
import random
from abc import ABC, abstractmethod


class Organism(ABC):
    def __init__(self, name, strength, initiation, posX, posY, symbol, age, world):
        self._world = world
        self._age = age
        self._symbol = symbol
        self._initiation = initiation
        self._strength = strength
        self._name = name
        self._posY = posY
        self._posX = posX

    def getName(self):
        return self._name

    def getStrength(self):
        return self._strength

    def setStrength(self, strength):
        self._strength = strength

    def getInitiation(self):
        return self._initiation

    def getPosX(self):
        return self._posX

    def setPosX(self, posX):
        self._posX = posX

    def getPosY(self):
        return self._posY

    def setPosY(self, posY):
        self._posY = posY

    def getSymbol(self):
        return self._symbol

    def getAge(self):
        return self._age

    def setWorld(self, world):
        self._world = world

    def getNewXY(self, newXY, range):
        if self._world.isHex():
            while True:
                newXY[0] = self._posX + random.randint(-range, range)
                newXY[1] = self._posY + random.randint(-range, range)

                if self._posY % 2 == 1:
                    if (newXY[0] == self._posX + 1 and newXY[1] == self._posY + 1) or \
                            (newXY[0] == self._posX + 1 and newXY[1] == self._posY - 1):
                        continue
                else:
                    if (newXY[0] == self._posX - 1 and newXY[1] == self._posY + 1) or \
                            (newXY[0] == self._posX - 1 and newXY[1] == self._posY - 1):
                        continue
                if newXY[0] >= self._world.getSizeX() or newXY[0] < 0 or \
                        newXY[1] >= self._world.getSizeY() or newXY[0] < 0 or \
                        (newXY[0] == self._posX and newXY == self._posY):
                    continue
                break
        else:
            while True:
                newXY[0] = self._posX + random.randint(0, range*2) - range
                newXY[1] = self._posY + random.randint(0, range*2) - range
                if (self._world.getSizeX() > newXY[0] >= 0 and
                        self._world.getSizeY() > newXY[1] >= 0 and
                        (newXY[0] != self._posX or newXY[1] != self._posY)):
                    break

    def yearOlder(self, years):
        self._age += years

    def proliferation(self, attacker):
        if (self.__class__ == attacker.__class__ and
                self != attacker and
                self._age >= 10 and
                attacker.getAge() > 10 and
                random.randint(0, self._age) < math.sqrt(self._age)):
            newXY = [0, 0]
            i = 0
            while True:
                self.getNewXY(newXY, 1)
                i = i + 1
                if self._world.getCell(newXY[0], newXY[1]) is not None and i < 100:
                    continue
                break
            if i < 100:
                temp = self.__class__(0, 0, None)
                temp.setPosX(newXY[0])
                temp.setPosY(newXY[1])
                self._world.insertOrganism(temp)
                print(self._name + '(' + str(self._posX) + ',' + str(self._posY) + ')' + " rozmnozyl sie z " +
                            attacker._name + '(' + str(attacker._posX) + ',' + str(attacker._posY) + ')' + " rodzac " +
                            temp._name + '(' + str(temp.getPosX()) + ',' + str(temp.getPosY()) + ')');
        if self.__class__ != attacker.__class__:
            return False
        else:
            return True

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, attacker):
        pass

    @abstractmethod
    def move(self, newX, newY):
        pass

    def __str__(self):
        return "({},{})".format(self._posX, self._posY)
