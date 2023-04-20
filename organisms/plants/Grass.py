from organisms.Plants import Plants


class Grass(Plants):
    def __init__(self, posX, posY, world):
        super().__init__("Trawa", 0, 0, posX, posY, "t", 0, world)