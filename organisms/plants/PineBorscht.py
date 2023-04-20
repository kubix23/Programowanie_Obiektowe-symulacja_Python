import random

from organisms.Animals import Animals
from organisms.Plants import Plants


class PineBorscht(Plants):
    def __init__(self, posX, posY, world):
        super().__init__("BarszczSosnowskiego", 10, 0, posX, posY, "s", 0, world)

    def action(self):
        for i in range(-1,2):
            for j in range(-1, 2):
                if self._world.isHex():
                    if self._posY%2 == 0:
                        if (i == -1 and j == -1) or (i == 1 and j == -1):
                            continue
                    else:
                        if (i == -1 and j == 1) or (i == 1 and j == 1):
                            continue
                if self._world.getSizeX() > self._posX + j >= 0 and \
                        self._world.getSizeY() > self._posY + i >= 0:
                    temp = self._world.getCell(self._posX + j, self._posY + i)
                    if temp is not None:
                        if isinstance(temp,Animals):
                            temp.collision(self)
        if random.randint(0, 8) == 0:
            self.proliferation(self)
