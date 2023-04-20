from abc import ABC

from organisms.Organism import Organism


class Animals(Organism, ABC):
    def __int__(self, name, strength, initiation, posX, posY, symbol, age, world):
        super().__init__(name, strength, initiation, posX, posY, symbol, age, world)

    def move(self, newX, newY):
        if self._world.getCell(newX, newY) is not None:
            self._world.getCell(newX, newY).collision(self)
        else:
            self._world.setCell(self._posX, self._posY, None)
            self._world.setCell(newX, newY, self)
            self._posX = newX
            self._posY = newY

    def action(self):
        newXY = [0, 0]
        self.getNewXY(newXY, 1)
        self.move(newXY[0], newXY[1])

    def collision(self, attacker):
        if not self.proliferation(attacker):
            print(str(attacker._name) + '(' + str(attacker._posX) + ',' + str(attacker._posY) + ')' + " zaatakowal " +
             str(self._name) + '(' + str(self._posX) + ',' + str(self._posY) + ')', end='')
            if attacker.getStrength() >= self._strength:
                newX = self._posX
                newY = self._posY
                self._world.removeOrganism(self)
                attacker.move(newX, newY)
                print(" wygrywajac")
            else:
                self._world.removeOrganism(attacker)
                print(" przegrywajac")
