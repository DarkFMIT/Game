from game import Game
from screen_opti import Screen
from objects_for_build import Objects_for_build
from house import House
from road import Road
from cemetery import Cemetery
from university import University
from school import School
from church import Church
from police import Police
from firestation import Firestation
from menu_test import  Menu
from hospital import Hospital
from dump import Dump
from president import President
from factory import Factory
import pygame
pygame.font.init()

def choose_build(razdel):
    global menu, screen
    if razdel == 1:
        if menu.number == 1:
            building = Cemetery(screen, position, "Cemetery")
        if menu.number == 2:
            building = Church(screen, position, "Church_1")
        if menu.number == 3:
            building = Church(screen, position, "Church_2")
        if menu.number == 4:
            building = Dump(screen, position, "Dump")
        if menu.number == 5:
            building = Firestation(screen, position, "Fire")
        if menu.number == 6:
            building = Hospital(screen, position, "Hospital")
        if menu.number == 7:
            building = Police(screen, position, "Police")
        if menu.number == 8:
            building = President(screen, position, "President")
        if menu.number == 9:
            building = School(screen, position, "School_1")
        if menu.number == 10:
            building = School(screen, position, "School_2")
        if menu.number == 11:
            building = University(screen, position, "University_vip")
    if razdel == 2:
        building = House(screen, position, f"House_{menu.number}")
    if razdel == 3:
        building = Factory(screen, position, f"Factory_{menu.number}")
    return building


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
                            print(menu.num_razd, menu.number)
                            new_build = choose_build(menu.num_razd)
                            new_build.buy()
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and screen.prev_x != -2:
            points = screen.get_romb(position)
            if (not(type(game.all_plates[points[0]][points[1]]) == int)):
                screen.delete_build(game.all_plates[points[0]][points[1]])
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