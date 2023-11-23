import pygame
from screen import Screen
from game import Game
from house import House
from road import Road

game = Game()
Sc = Screen(game)
x = 0
y = 0
x_for_lines = 0
y_for_lines = 0
position = pygame.draw.lines(Sc.screen, (0, 0, 0), True,
    [[x + 60, y], [x + 120, y + 30], [x + 60, y + 60], [x, y + 30]], 2)

prev_x = -1
prev_y = -1 
done = False
print(*game.all_plates, sep='\n')
Sc.update_window()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
                            moving = Sc.move(moving)
                            Sc.update_window()
            if event.button == 1:
                Sc.mark_plate(event.pos)
                print(x, y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b and prev_x != -2:
            moving = [x + 1, y + 1]
            house = House(moving, Sc)  # Передаем Sc как параметр
            Sc.mark_plate([x, y])
            house.buy_house()
            Sc.update_window()
            prev_x = -2
            
    pygame.display.flip()
