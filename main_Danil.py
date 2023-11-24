from game import Game
from screen import Screen
from objects_for_build import Objects_for_build
from house import House
import pygame

class Menu(Screen):
    def __init__(self, screen):
        self.menu = pygame.image.load(".\Menu.png")
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


game = Game()
screen = Screen(game)
done = False
screen.update_window()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                pygame.mouse.get_rel()
                while pygame.mouse.get_pressed():
                    events = pygame.event.get()
                    if(len(events) != 0):
                        if pygame.mouse.get_pressed()[2] == 0:
                            break
                        else:
                            moving = pygame.mouse.get_rel()
                            moving = screen.move(moving)
                            screen.update_window()
                            if screen.prev_x != -2:
                                x = position[0] - moving[0]
                                y = position[1] - moving[1]
                                screen.mark_plate([x, y])
                                position = screen.mark_plate([x, y])
            if event.button == 1:
                position = screen.mark_plate(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b and screen.prev_x != -2:
            house = House(screen, position)
            house.buy()
            screen.update_window()
            prev_x = -2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m and screen.prev_x != -2:
            menu = Menu(screen)
            position = menu.centre(position)
            
    pygame.display.flip()