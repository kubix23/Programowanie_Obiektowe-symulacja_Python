from organisms.Plants import Plants


class Belladonna(Plants):
    def __init__(self, posX, posY, world):
        super().__init__("WilczaJagoda", 99, 0, posX, posY, "j", 0, world)

    def collision(self, attacker):
        super().collision(attacker)
        if attacker.getStrength() < self._strength:
            self._world.removeOrganism(self)