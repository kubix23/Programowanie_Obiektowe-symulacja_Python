import pygame

from view.EventList import EventList


class Control(pygame.sprite.Sprite):
    def __init__(self, x, y, world, group):
        self.__x = x
        self.__y = y
        self.__world = world
        self.__width = pygame.display.get_surface().get_width() - x
        self.__height = pygame.display.get_surface().get_height() - y
        self.__smallfont = pygame.font.SysFont('Corbel', int(self.__height / 3))
        self.rect = pygame.rect.Rect(x, y, self.__width, self.__height)
        self.image = pygame.Surface((self.__width, self.__height))
        self._layer = 2
        self.__button = []
        self.printButton(0, 0, 0, self.__width / 3, self.__height, (255, 255, 255),"Next")
        self.printButton(1, self.__width / 3, 0, self.__width / 3, self.__height, (255, 255, 0), "Save")
        self.printButton(2, 2 * self.__width / 3, 0, self.__width / 3, self.__height, (255, 0, 255), "Load")
        pygame.sprite.Sprite.__init__(self, group)
        EventList.add(self)

    def printButton(self, i, x, y, width, height, color=(255, 255, 255),stri = ""):
        temp = pygame.draw.rect(self.image, color, [x, y, width, height])
        temp.x += self.__x
        temp.y += self.__y
        self.__button.insert(i, temp)
        text = self.__smallfont.render(stri, True, (0, 0, 0))
        self.image.blit(text, (x + width/2 - text.get_width() / 2, y + height / 2 - text.get_height() / 2))

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if self.__button[0].collidepoint(pos):
                self.__world.takeTurn()
            elif self.__button[1].collidepoint(pos):
                self.__world.save()
            elif self.__button[2].collidepoint(pos):
                self.__world.load()