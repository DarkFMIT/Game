from game import Game
from screen import Screen
from objects_for_build import Objects_for_build
from house import House
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
            house = House(screen, position) # Ошибка в координатах
            house.buy()
            screen.update_window()
            prev_x = -2
            
    pygame.display.flip()