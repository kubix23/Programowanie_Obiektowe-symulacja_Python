from organisms.Animals import Animals


class Fox(Animals):
    def __init__(self, posX, posY, world):
        super().__init__("Lis", 3, 7, posX, posY, "L", 0, world)

    def action(self):
        newXY = [0,0]
        i = 0
        while True:
            self.getNewXY(newXY,1)
            i += 1
            if self._world.getCell(newXY[0], newXY[1]) is None or\
                    self._world.getCell(newXY[0], newXY[1]).getStrength() <= self._strength or\
                    i > 100:
                break
        if i >= 100:
            return
        self.move(newXY[0],newXY[1])