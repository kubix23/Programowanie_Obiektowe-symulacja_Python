from organisms.Animals import Animals


class Wolf(Animals):
    def __init__(self, posX, posY, world):
        super().__init__("Wilk", 9, 5, posX, posY, "W", 0, world)
