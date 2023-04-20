from organisms.Plants import Plants


class Guarana(Plants):
    def __init__(self, posX, posY, world):
        super().__init__("Guarana", 0, 0, posX, posY, "g", 0, world)

    def collision(self, attacker):
        attacker.setStrength(attacker.getStrength() + 3)
        super().collision(attacker)