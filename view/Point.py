import math

import pygame
from view.EventList import EventList
from view.SelectMenu import SelectMenu



class Point(pygame.sprite.Sprite):
    def __init__(self, parent, group, layer, x, y, width, height, world, path, posX, posY):
        self.__path = []
        minX = path[0][0]
        minY = path[0][0]
        for p in path:
            minX = min(minX,p[0])
            minY = min(minY, p[1])
        for p in path:
            xx = p[0] + (minX * (p[0]-width/2)/(width/2 - minX))
            yy = p[1] + (minY * (p[1] - height / 2) / (height / 2 - minY))
            self.__path.append((xx, yy))
        self._name = None
        self.__popUp = None
        self.__parent = parent
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))
        self._layer = layer
        self.__mouseOver = False
        self.__menu = False
        self.__smallfont = pygame.font.SysFont('Corbel', int(min(width, height)/2))
        self.__posX = posX
        self.__posY = posY
        self.__world = world
        self.setName(self._name)
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_colorkey(None)
        pygame.sprite.Sprite.__init__(self, group)
        EventList.add(self)

    def setName(self, name, bacground=(255, 255, 255)):
        self._name = name
        self.image.set_colorkey((0,0,0))
        contrast = (255-bacground[0], 255-bacground[1], 255-bacground[2])
        text = self.__smallfont.render(name, True, contrast)
        pygame.draw.polygon(self.image, bacground, self.__path)
        pygame.draw.polygon(self.image, (1,1,1), self.__path, 4)
        self.image.blit(text, (self.image.get_width() / 2 - text.get_width() / 2, self.image.get_width() / 2 - text.get_height() / 2))
        self.update()

    def event(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION and not self.__menu:
            if self.rect.collidepoint(pos) and self.mask.get_at((pos[0] - self.rect.x, pos[1] - self.rect.y)):
                self.__mouseOver = True
                self.setName(self._name, (255, 0, 255))

            elif self.__mouseOver:
                self.__mouseOver = False
                self.setName(self._name)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if not self.__parent.getPopup().collidepoint(pos):
                    if self.rect.collidepoint(pos) and self.mask.get_at((pos[0] - self.rect.x, pos[1] - self.rect.y)):
                        if not self.__menu and self._name == None:
                            self.__menu = True
                            self.__popUp = SelectMenu(self.groups(), self._layer + 1, pos[0] + 1, pos[1] + 1,
                                                      self.__posX, self.__posY, self.__world)
                            self.__parent.setPopup(self.__popUp.rect)
                            self.setName(self._name, (255, 0, 0))
                    elif self.__menu:
                        self.__menu = False
                        self.__popUp.event(event)
                        EventList.remove(self.__popUp)
                        self.__popUp.kill()
                        self.setName(self._name)
                        pygame.display.update()
            else:
                if self.__menu:
                    self.__menu = False
                    self.__popUp.event(event)
                    EventList.remove(self.__popUp)
                    self.__popUp.kill()
                    self.setName(self._name)
                    self.__parent.setPopup(pygame.rect.Rect(0, 0, 0, 0))
                    pygame.display.update()

