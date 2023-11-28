from game import Game
from screen import Screen
from objects_for_build import Objects_for_build
from house import House
from road import Road
from menu import Menu
import pygame


            


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
                screen.prev_x = -2
                while pygame.mouse.get_pressed():
                    events = pygame.event.get()
                    if(len(events) != 0):
                        if pygame.mouse.get_pressed()[2] == 0:
                            break
                        else:
                            moving = pygame.mouse.get_rel()
                            moving = screen.move(moving)
                            screen.update_window()
            if event.button == 1:
                position = screen.mark_plate(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b and screen.prev_x != -2:
            road = Road(screen, position)
            road.buy()
            screen.update_window()
            screen.prev_x = -2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h and screen.prev_x != -2:
            house = House(screen, position)
            house.buy()
            screen.update_window()
            screen.prev_x = -2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m and screen.prev_x != -2:
            menu = Menu(screen)
            position = menu.show_menu(position)
            
    pygame.display.flip()