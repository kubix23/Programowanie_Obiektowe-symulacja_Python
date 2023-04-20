from organisms.Animals import Animals
from organisms.plants.PineBorscht import PineBorscht


class CyberOwca(Animals):
    def __init__(self, posX, posY, world):
        super().__init__("CyberOwca", 11, 4, posX, posY, "CO", 0, world)

    def action(self):
        newXY = [0, 0]
        target = None
        for o in self._world.getOrganisms():
            if isinstance(o, PineBorscht):
                target = o
                break
        for o in self._world.getOrganisms():
            if isinstance(o, PineBorscht):
                if min(max(o.getPosX(), o.getPosY()), max(target.getPosX(), target.getPosY())) != max(target.getPosX(), target.getPosY()):
                    target = o

        if target is not None:
            x = target.getPosX() - self._posX
            y = target.getPosY() - self._posY
            newXY[0] = 0 if x == 0 else x/abs(x)
            newXY[0] += self._posX
            newXY[1] = 0 if y == 0 else y/abs(y)
            newXY[1] += self._posY
        else:
            self.getNewXY(newXY,1)

        self.move(newXY[0], newXY[1])
        
    def collision(self, attacker):
        if attacker.__class__ is PineBorscht:
            return
        super(CyberOwca, self).collision(attacker)