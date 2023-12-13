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
from menu import  Menu
from hospital import Hospital
from dump import Dump
from president import President
from factory import Factory
from pump import Pump
import pygame
from time import sleep as zZz
pygame.font.init()

def wheell(total_time):
    time = 0
    while time < total_time:
        for i in range(0, 24):
            yield i
            time += 1

def loading(screen):
    previu = pygame.image.load("./resources/previu.png")
    screen.window.blit(previu, (0, 0))
    pygame.display.flip()
    zZz(3)
    waiting(screen)

def start_menu(screen):
    flag = False
    previu = pygame.image.load("./resources/previu.png")
    start_b = pygame.image.load("./resources/New_game.png")
    continue_b =  pygame.image.load("./resources/Continue.png")
    screen.window.blit(previu, (0, 0))
    screen.window.blit(start_b, (377, 281))
    screen.window.blit(continue_b, (377, 400))
    pygame.display.flip()
    while not flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coords = pygame.mouse.get_pos()
                    if (coords[0] >= 377) and (coords[0] <= 682):
                        if (coords[1] >= 281) and (coords[1] <= 354):
                            flag = True
                        if (coords[1] >= 400) and (coords[1] <= 473):
                            load_game(screen)
                            waiting(screen)
                            flag = True
    return False

def pause_menu(screen):
    flag = False
    previu = pygame.image.load("./resources/previu.png")
    save_b = pygame.image.load("./resources/Save_b.png")
    load_b =  pygame.image.load("./resources/Load.png")
    quit_b =  pygame.image.load("./resources/Quit.png")
    screen.window.blit(previu, (0, 0))
    screen.window.blit(save_b, (435, 200))
    screen.window.blit(load_b, (435, 300))
    screen.window.blit(quit_b, (435, 400))
    pygame.display.flip()
    while not flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coords = pygame.mouse.get_pos()
                    if (coords[0] >= 435) and (coords[0] <= 625):
                        if (coords[1] >= 200) and (coords[1] <= 274):
                            save_game(screen)
                            flag = True
                        if (coords[1] >= 300) and (coords[1] <= 374):
                            load_game(screen)
                            waiting(screen)
                            flag = True
                        if (coords[1] >= 400) and (coords[1] <= 474):
                            return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                flag = True
    return False                                               

def waiting(screen):
    previu = pygame.image.load("./resources/previu.png")
    repeat = wheell(162)
    for i in repeat:
        image = pygame.image.load(f"./loading/{i}.png") 
        screen.window.blit(previu, (0, 0))
        screen.window.blit(image, (281, 300))
        zZz(0.1)
        pygame.display.flip()


    

def choose_build(menu, screen, position, razdel):
    if razdel == 1:
        if menu.number == 1:
            building = Cemetery(screen, position, "Cemetery")
        if menu.number == 2:
            building = Church(screen, position, "Church_1")
        if menu.number == 3:
            building = Church(screen, position, "Church_2")
        if menu.number == 4:
            building = Pump(screen, position, "Pump")
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
        if menu.number == 12:
            building = Dump(screen, position, "Dump")
    if razdel == 2:
        building = House(screen, position, f"House_{menu.number}")
        building.prise = int(menu.number ** 0.8 * building.prise)
        building.capacity = int(menu.number ** 0.5 * building.capacity)
    if razdel == 3:
        building = Factory(screen, position, f"Factory_{menu.number}")
        building.workspace = 3 * int(menu.number ** 0.5 * building.workspace)
        building.prise = int(menu.number ** 0.8 * building.workspace)
        building.default_income = menu.number * building.default_income
    return building

def save_game(screen):
    with open("./resources/Save/save", "wt") as file:
        file.write(str(screen.game) + "\n")
        file.write(str(screen) + "\n")
        for i in range(80):
            for j in range(80):
                if type(screen.game.all_plates[i][j]) != int:
                    file.write(str(screen.game.all_plates[i][j]) + "\n")

def load_game(screen):
    game = Game()
    screen.game = game
    with open("./resources/Save/save", "rt") as file:
        list_save = file.readlines()
    screen.game.load(list_save[0])
    screen.load(list_save[1])
    for i in range(2, len(list_save)):
        building = choose_class(list_save[i].split("|")[0], screen)
        building.load(list_save[i])
        tmp_build = building.points_for_build
        tmp_build[0] += 60
        tmp_build[1] += 170
        place_in_matrix = screen.get_romb(tmp_build)
        tmp_build[0] -= 60
        tmp_build[1] -= 170
        screen.game.all_plates[place_in_matrix[0]][place_in_matrix[1]] = building


def choose_class(name_of_class, screen):
    match name_of_class:
        case "House":
            building = House(screen, [0, 0], "Dump")
        case "Cemetery":
            building = Cemetery(screen, [0, 0], "Dump")
        case "Dump":
            building = Dump(screen, [0, 0], "Pump")
        case "Church":
            building = Church(screen, [0, 0], "Dump")
        case "Pump":
            building = Pump(screen, [0, 0], "Pump")
        case "Factory":
            building = Factory(screen, [0, 0], "Dump")
        case "Firestation":
            building = Firestation(screen, [0, 0], "Dump")
        case "Hospital":
            building = Hospital(screen, [0, 0], "Dump")
        case "Police":
            building = Police(screen, [0, 0], "Dump")
        case "President":
            building = President(screen, [0, 0], "Dump")
        case "School":
            building = School(screen, [0, 0], "Dump")
        case "University":
            building = University(screen, [0, 0], "Dump")
        case "Road":
            building = Road(screen, [0, 0])
    return building