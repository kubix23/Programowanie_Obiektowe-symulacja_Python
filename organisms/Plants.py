import random

from organisms.Organism import Organism


class Plants(Organism):
    def __int__(self, name, strength, initiation, posX, posY, symbol, age, world):
        super().__init__(name, strength, initiation, posX, posY, symbol, age, world)

    def move(self, newX, newY):
        pass

    def action(self):
        if random.randint(0, 4) == 0:
            self.proliferation(self)

    def collision(self, attacker):
        print(attacker._name + '(' + str(attacker._posX) + ',' + str(attacker._posY) + ')' + " zblizyl sie do " +
                    self._name + '(' + str(self._posX) + ',' + str(self._posY) + ')', end='')
        if attacker.getStrength() >= self._strength:
            newX = self._posX
            newY = self._posY
            self._world.removeOrganism(self)
            attacker.move(newX, newY)
            print(" i go zjadl")
        else:
            self._world.removeOrganism(attacker)
            print(" i przegral z roslina")
