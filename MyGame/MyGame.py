import pygame
pygame.init()
class Game:
        time = 0
        money = 200000
        all_plates = [[0 for i in range(60)] for i in range(60)]
        all_plates[0][0] = 1
        def buy(self):
                points = self.get_romb(self.coords)
                if not(self.game.all_plates[points[0]][points[1]] in self.dopusc):
                     return 0
                if self.game.money < self.prise:
                     return 1
                self.money -= self.prise
                self.game.all_plates[points[0]][points[1]] = self       
        def randTick(self):
                self.time += 1

class Screen(Game):
    X_glob = 0
    Y_glob = 0
    screen = pygame.display.set_mode((1060, 600))
    grass = pygame.image.load(".\MyGame\grass_grid.jpg")

    "Экран ҫӗнетни. Вӑйӑ хирне таврӑнмалла"    
    def update_window(self):
        self.screen.blit(self.grass, (self.X_glob, self.Y_glob))
        for i in range(52):
             for j in range(42):
                  something = self.all_plates[j][i]
                  if type(something) != int:
                       self.screen.blit(something.type, (something.coords[0], something.coords[1] - 140))
        pygame.display.flip()
    
    "Экрана тата пур объекта та (ҫуртсене, ҫулсене, курсора)куҫарса лартассишӗн яваплӑ функци"
    def move(self, moving):
        tmp_x = self.X_glob
        tmp_y = self.Y_glob
        if self.X_glob + moving[0] <= 0 and self.X_glob + moving[0] >= 1060 - 2500:
            self.X_glob += moving[0]
        if self.X_glob > 0:
              self.X_glob = 0
        if self.X_glob < 1060 - 2500:
              self.X_glob = 1060 - 2500
        if self.Y_glob + moving[0] <= 0 and self.Y_glob + moving[0] >= 600 - 1500:
            self.Y_glob += moving[1]
        if self.Y_glob > 0:
              self.Y_glob = 0
        if self.Y_glob < 600 - 1500:
              self.Y_glob = 600 - 1500
        tmp_x = tmp_x - self.X_glob
        tmp_y = tmp_y - self.Y_glob
        for lines in self.all_plates:
            for something in lines:
                if type(something) != int:
                        something.coords[0] -= tmp_x
                        something.coords[1] -= tmp_y
        return [tmp_x, tmp_y]
    
    "Вӑйӑ хирӗнчи кликпа ромб вырӑнне шайлаштарма май парать"
    def get_romb(self, points):
        global Sc
        x = points[0] - Sc.X_glob 
        y = points[1] - Sc.Y_glob
        if (x // 60 + y // 30) % 2 == 0:
            x_1 = (x // 60) * 60
            y_1 = (y // 30 + 1) * 30
            y_vaive = y_1 + (x_1 - x) * 3 ** 0.5 / 3
            if(y_vaive > y):
                Up = True
            else:
                Up = False
            if Up:
                x_return = x // 60 - 1
                y_return = y // 30 - 1
            else:
                x_return = x // 60
                y_return = y // 30
        else:
            x_1 = (x // 60) * 60
            y_1 = (y // 30) * 30
            y_vaive = y_1 + (x - x_1) * 3 ** 0.5 / 3
            if(y_vaive > y):
                Up = True
            else:
                Up = False
            if Up:
                x_return = x // 60
                y_return = y // 30 - 1
            else:
                x_return = x // 60 - 1
                y_return = y // 30
        return [x_return, y_return]

    
    "Функци эпир пуснӑ ромбран уйӑрать, тепӗр хут кӑшкӑрсан, уйӑрӑлӑва пуҫтарать."
    def mark_plate(self, pos):
        global x, y, prev_x, prev_y, game, position
        points = self.get_romb(pos)
        if points[0] == prev_x and points[1] == prev_y:
            prev_x = -2
            prev_y = -2
            self.update_window()
        else:
            prev_x = points[0]
            prev_y = points[1]
            x = points[0] * 60 + self.X_glob
            y = points[1] * 30 + self.Y_glob
            print(points)
            self.update_window()
            if game.all_plates[points[0]][points[1]] != 1:
                position = pygame.draw.lines(self.screen, (0,0,0), True,
                    [[x + 60, y], [x + 120, y + 30], [x + 60, y + 60], [x, y + 30]], 2)
    def drawing(self, points, screen):
        print(0)
        screen.screen.blit(self.type, (points[0], points[1] - 140))

class Objects_for_build(Screen):
        pass

class House(Objects_for_build):
        global game, Sc
        def __init__(self, coords):
            self.coords = coords
            self.type = pygame.image.load(".\MyGame\house.png")
            self.game = game
            self.prise = 100
            self.key = "house" 
            self.screen = Sc
            self.dopusc = [0, 2]
        def buy_house(self):
            self.buy()

            

game = Game()
Sc = Screen()
x = 0
y = 0
position = pygame.draw.lines(Sc.screen, (0,0,0), True,
    [[x + 60, y], [x + 120, y + 30], [x + 60, y + 60], [x, y + 30]], 2)


prev_x = -1
prev_y = -1 
done = False
print(*game.all_plates, sep = '\n')
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
                    #print(events)
                    if(len(events) != 0):
                        if pygame.mouse.get_pressed()[2] == 0:
                            break
                        else:
                            moving = pygame.mouse.get_rel()
                            moving = Sc.move(moving)
                            x = x - moving[0]
                            y = y - moving[1]
                            Sc.update_window()
                            if(prev_x != -2):
                                position = pygame.draw.lines(Sc.screen, (0,0,0), True,
                                    [[x + 60, y], [x + 120, y + 30], [x + 60, y + 60], [x, y + 30]], 2)
            if event.button == 1:
                Sc.mark_plate(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b and prev_x != -2:
            moving = [x, y]
            house = House(moving) # Ошибка в координатах
            Sc.mark_plate([x,y])
            house.buy_house()
            Sc.update_window()
    pygame.display.flip()