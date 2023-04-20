import pygame
from view.WindowGame import WindowGame
from world.World import World


if __name__ == '__main__':
    pygame.init()
    WindowGame(World(20, 20, True))
