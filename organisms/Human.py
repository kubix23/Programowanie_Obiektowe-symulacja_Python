import pygame

from organisms.Animals import Animals
from view.EventList import EventList

class Human(Animals):
    def __init__(self, posX, posY, world):
        self.__dx = 0
        self.__dy = 0
        self.__skillCooldown = 0
        super().__init__("Czlowiek", 5, 4, posX, posY, "@", 0, world)
        EventList.add(self)

    def moveSpeed(self, dx, dy):
        if self._world.isHex():
            if dy != 0:
                if self._posY % 2 == 0:
                    self.__dx = 1 if dx == 1 else 0
                else:
                    self.__dx = 0 if dx == 1 else -1
            else:
                self.__dx = dx
            self.__dy = dy
        else:
            self.__dx = dx if dx != 0 else self.__dx
            self.__dy = dy if dy != 0 else self.__dy

    def action(self):
        if self.__dx != 0 or self.__dy != 0:
            newY = self._posY + self.__dy
            newX = self._posX + self.__dx
            if 0 <= newY < self._world.getSizeY() and \
                    0 <= newX < self._world.getSizeX():
                self.move(newX, newY)
            self.__dx = 0
            self.__dy = 0
        if self.__skillCooldown != 0:
            self.__skillCooldown -= 1
            print("Zostalo " + str(self.__skillCooldown) + " lat do uzycia Calopalenia");

    def skill(self):
        if self.__skillCooldown == 0:
            print("Czlowiek uzyl umiejetnosci Calopalenie niszczac:");
            self.__skillCooldown = 5
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if self._world.isHex():
                        if self._posY % 2 == 0:
                            if (i == -1 and j == -1) or (i == 1 and j == -1):
                                continue
                        else:
                            if (i == -1 and j == 1) or (i == 1 and j == 1):
                                continue
                    if self._world.getSizeX() > self._posX + j >= 0 and \
                            self._world.getSizeY() > self._posY + i >= 0:
                        temp = self._world.getCell(self._posX + j, self._posY + i)
                        if temp is not None and temp is not self:
                            print("\t--" + temp.getName() + '(' + str(temp.getPosX()) + ',' + str(temp.getPosY()) + ')')
                            self._world.removeOrganism(temp)
            self._world.updateWorld()
        else:
            print("Zostalo " + str(self.__skillCooldown) + " lat do uzycia Calopalenia")

    def event(self,event):
        if event.type == pygame.KEYDOWN:
            if self._world.isHex():
                if pygame.key.get_pressed()[pygame.K_q]:
                    self.moveSpeed(-1, -1);
                if pygame.key.get_pressed()[pygame.K_w]:
                    self.moveSpeed(1, -1);
                if pygame.key.get_pressed()[pygame.K_a]:
                    self.moveSpeed(-1, 0);
                if pygame.key.get_pressed()[pygame.K_s]:
                    self.moveSpeed(1, 0);
                if pygame.key.get_pressed()[pygame.K_z]:
                    self.moveSpeed(-1, 1);
                if pygame.key.get_pressed()[pygame.K_x]:
                    self.moveSpeed(1, 1);
                if pygame.key.get_pressed()[pygame.K_p]:
                    self.skill()
            else:
                if pygame.key.get_pressed()[pygame.K_UP]:
                    self.moveSpeed(0, -1);
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.moveSpeed(-1, 0);
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.moveSpeed(1, 0);
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.moveSpeed(0, 1);
                if pygame.key.get_pressed()[pygame.K_p]:
                    self.skill()
