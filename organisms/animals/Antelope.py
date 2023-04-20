import random

from organisms.Animals import Animals


class Antelope(Animals):
    def __init__(self, posX, posY, world):
        super().__init__("Antylopa", 4, 4, posX, posY, "A", 0, world)

    def action(self):
        newXY = [0, 0]
        self.getNewXY(newXY, 2)
        self.move(newXY[0], newXY[1])

    def collision(self, attacker):
        if not self.proliferation(attacker):
            print(attacker.getName() + '(' + str(attacker.getPosX()) + ',' + str(attacker.getPosY()) + ')' + " zaatakowal " + self._name + '(' + str(self._posX) + ',' + str(self._posY) + ')', end='')
            if random.randint(0,2) == 1:
                newXY = [0,0]
                i = 0
                while True:
                    self.getNewXY(newXY, 1)
                    i += 1
                    if self._world.getCell(newXY[0], newXY[1]) is not None or\
                        i > 100:
                        break
                if i > 100:
                    return
                self.move(newXY[0], newXY[1])
            else:
                super().collision(attacker)