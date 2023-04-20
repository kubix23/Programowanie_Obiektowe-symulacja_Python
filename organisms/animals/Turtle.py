from organisms.Animals import Animals


class Turtle(Animals):
    def __init__(self, posX, posY, world):
        super().__init__("Zolw", 2, 1, posX, posY, "Z", 0, world)

    def collision(self, attacker):
        if not self.proliferation(attacker):
            print(attacker.getName() + '(' + str(attacker.getPosX()) + ',' + str(attacker.getPosY()) + ')' + " zaatakowal " +
             self._name + '(' + str(self._posX) + ',' + str(self._posY) + ')', end='')
            if attacker.getStrength() >= 5 and attacker.getStrength() >= self._strength:
                newX = self._posX
                newY = self._posY
                self._world.removeOrganism(self)
                attacker.move(newX, newY)
                print(" wygrywajac")
            else:
                print(" remisujac")