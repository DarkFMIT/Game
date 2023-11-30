from game import Game
from screen_opti import Screen
from objects_for_build import Objects_for_build
from house import House
from road import Road
from menu_test import  Menu
from hospital import Hospital
import pygame
pygame.font.init()




game = Game()
screen = Screen(game)
menu = Menu(screen)
done = False
screen.update_window()
while not done:
    game.add_time()
    menu.update_menu()
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
                    game.add_time()
                    menu.update_menu()
            if event.button == 1:
                if event.pos[1] > screen.size[1] - 30:
                    if (screen.prev_x != -2):
                        menu.choose(event.pos, position)
                        if menu.flag:
                            house = House(screen, position, f"House_{menu.number}")
                            house.buy()
                            screen.update_window()
                            menu.update_menu()
                            screen.prev_x = -2
                            menu.flag = False

                else:
                    position = screen.mark_plate(event.pos)
                    menu.update_menu()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b and screen.prev_x != -2:
            road = Road(screen, position)
            road.buy()
            screen.update_window()
            menu.update_menu()
            screen.prev_x = -2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h and screen.prev_x != -2:
            house = House(screen, position, "House_1")
            house.buy()
            screen.update_window()
            menu.update_menu()
            screen.prev_x = -2
                   # ПРОВЕРКА ГОСПИТАЛЯ
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c and screen.prev_x != -2:
            hospital = Hospital(screen, position, "Hospital")
            hospital.buy()
            screen.update_window()
            menu.update_menu()
            screen.prev_x = -2
    pygame.display.flip()