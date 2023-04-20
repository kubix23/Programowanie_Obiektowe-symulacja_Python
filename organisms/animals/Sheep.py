from organisms.Animals import Animals


class Sheep(Animals):
    def __init__(self, posX, posY, world):
        super().__init__("Owca", 4, 4, posX, posY, "O", 0, world)
