import pygame





X_glob = 0
Y_glob = 0
pygame.init()
screen = pygame.display.set_mode((1060, 600))
grass = pygame.image.load(".\Game\MyGame\grass.jpg")
house = pygame.image.load(".\Game\MyGame\house.png")
objects_on_screen = {}
objects = {}
objects['house'] = house
objects_on_screen["house"] = []

def update_window():
    screen.blit(grass,(X_glob,Y_glob))
    for key in objects_on_screen.keys():
           for points in objects_on_screen[key]:
                  screen.blit(objects[key], (points[0], points[1]))
    pygame.display.flip()
def add_house(x, y):
    objects_on_screen["house"].append([x, y])

def move_screen(moving):
        global X_glob, Y_glob
        tmp_x = X_glob
        tmp_y = Y_glob
        if X_glob + moving[0] <= 0 and X_glob + moving[0] >= 1060 - 2500:
            X_glob += moving[0]
        if X_glob > 0:
              X_glob = 0
        if X_glob < 1060-2500:
              X_glob = 1060-2500
        if Y_glob + moving[0] <= 0 and Y_glob + moving[0] >= 600 - 1500:
            Y_glob += moving[1]
        if Y_glob > 0:
              Y_glob = 0
        if Y_glob < 600-1500:
              Y_glob = 600-1500
        return [tmp_x - X_glob, tmp_y - Y_glob]

done = False
is_blue = True
x = 0
y = 0

update_window()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP: 
                        y -= 60
                        update_window()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                        y += 60
                        update_window()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        x -= 60
                        update_window()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: 
                        x += 60
                        update_window()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER: 
                        add_house(x, y)
                        update_window()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            print(X_glob)
                            print(Y_glob)
                            x = (-X_glob + event.pos[0]) // 60 * 60 + X_glob
                            y = (-Y_glob  +event.pos[1]) // 60 * 60 + Y_glob
                            print(pygame.mouse.get_rel())
                            update_window()
                        if event.button == 3:
                            pygame.mouse.get_rel()
                            while pygame.mouse.get_pressed():
                                g = pygame.event.get()
                                if(len(g) != 0):
                                       if pygame.mouse.get_pressed()[2] == 0:
                                              break
                                       else:
                                            move = pygame.mouse.get_rel()
                                            position = pygame.draw.lines(screen, (0,0,0), True,
                                                [[x, y], [x + 60, y], [x + 60, y + 60], [x, y + 60]], 2)  
                                            move = move_screen(move)
                                            x=x-move[0]
                                            y=y-move[1]
                                            update_window()

                       
        
        position = pygame.draw.lines(screen, (0,0,0), True,
                  [[x, y], [x + 60, y], [x + 60, y + 60], [x, y + 60]], 2)
        
        pygame.display.flip()