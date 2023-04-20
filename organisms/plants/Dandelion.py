from organisms.Plants import Plants


class Dandelion(Plants):
    def __init__(self, posX, posY, world):
        super().__init__("Mlecz", 0, 0, posX, posY, "m", 0, world)

    def action(self):
        for i in range(0, 3):
            super().action()
