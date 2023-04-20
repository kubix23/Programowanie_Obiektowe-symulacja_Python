import glob
import importlib
import os
import time

import pygame
from view.EventList import EventList


class SelectMenu(pygame.sprite.Sprite):
    __table = []

    def __init__(self, group, layer, x, y, posX, posY, world):
        self.__button = []
        self.__width = 200
        self.__height = 300
        self.__x = posX
        self.__y = posY
        self.__smallfont = pygame.font.SysFont('Corbel', 25)
        self.__world = world
        self.__time = time.time()
        if self.__table == []:
            i = 0
            for file in glob.glob("./organisms/*/*.py"):
                name = os.path.splitext(os.path.basename(file))[0]
                self.__table.append(importlib.import_module("organisms." + os.path.basename(os.path.dirname(file)) + "." + name))
                i = i + 1

        if pygame.display.get_surface().get_rect().width - x < self.__width:
            x = pygame.display.get_surface().get_rect().width - self.__width
        if pygame.display.get_surface().get_rect().height - 100 - y < self.__height:
            y = pygame.display.get_surface().get_rect().height - 100 - self.__height

        self.image = pygame.Surface((self.__width, self.__height))
        self.rect = pygame.rect.Rect(x, y, self.__width, self.__height)
        for i in range(0, len(self.__table)):
            text = self.__smallfont.render("{}".format(self.__table[i].__name__.split(".")[-1]), True, (0, 0, 0))
            self.__button.append(pygame.draw.rect(self.image, (255, (255/len(self.__table))/(i+1), (255/len(self.__table))*i), [0, (self.__height/len(self.__table))*i, self.__width, self.__height/len(self.__table)]))
            self.image.blit(text, (self.__button[i].width/2 - text.get_width()/2, self.__button[i].y + self.__button[i].height/2 - text.get_height()/2))

        self._layer = layer
        pygame.sprite.Sprite.__init__(self, group)
        EventList.add(self)

    def event(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pos):
                if (time.time() - self.__time)*8 >= 4:
                    self.__time = time.time()
                    temp = [pos[0] - self.rect.x, pos[1] - self.rect.y]
                    for b in self.__button:
                        if b.collidepoint(temp):
                            org = self.__table[self.__button.index(b)]
                            self.__world.insertOrganism(getattr(org, org.__name__.split(".")[-1])(self.__x, self.__y, self.__world))
                            self.__world.updateWorld()
