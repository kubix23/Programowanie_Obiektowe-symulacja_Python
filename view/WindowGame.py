import pygame
from view.EventList import EventList
from view.WorldPanel import WorldPanel

class WindowGame:
    def __init__(self, world):
        self.__worldPanel = WorldPanel(world, world.isHex())
        world.setWorldPanel(self.__worldPanel)
