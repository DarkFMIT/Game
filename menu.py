from game import Game
from screen import Screen
from objects_for_build import Objects_for_build
from house import House
from road import Road
import pygame

class Menu(Screen):
    def __init__(self, screen):
        self.menu = pygame.image.load(".\\resources\Menu.png")
        self.screen = screen
    def centre(self, pos):
        x = self.screen.size[0] // 2 - pos[0]
        y = self.screen.size[1] // 2 - pos[1]
        moving = self.screen.move([x, y])
        self.screen.update_window()
        x = pos[0] - moving[0]
        y = pos[1] - moving[1]
        new_pos = self.screen.mark_plate([x, y])
        new_pos = self.screen.mark_plate([x, y])
        pygame.display.flip()
        return new_pos
    def show_menu(self, pos):
        pos = self.centre(pos)
        self.screen.window.blit(self.menu, (0, 550))
        pygame.display.flip()
        return(pos)