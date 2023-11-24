from objects_for_build import Objects_for_build
import pygame
class House(Objects_for_build):
    def __init__(self, screen, pos):
        icon = pygame.image.load(".\house.png")
        self.dopusc = [0, 2]
        self.prise = 1
        super().__init__(screen, pos, icon)
    def buy(self):
        self.screen.buy_building(self)
        