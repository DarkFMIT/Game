import pygame
pygame.init()
class Game:
        time = 0
        money = 2000000
        file = open('./MyGame/txt.txt', 'r+')
        all_plates = [[0 for i in range(90)] for i in range(90)]
        for i in range(20):
            str = file.readline().split()
            for j in range(len(str)):
                all_plates[i][j] = int(str[j])
                
        def buy(self):
                points = self.get_romb(self.coords)
                print(points)
                if not(self.game.all_plates[points[0]][points[1]] in self.dopusc):
                    self.can_not_build()
                    return 0
                if self.game.money < self.prise:
                    self.need_more_money(self.prise - self.money)
                    return 1
                
                self.money -= self.prise
                self = House(points)   
                self.game.all_plates[points[0]][points[1]] = self     
        
        def randTick(self):
                self.time += 1

        def need_more_money(self, money):
            pass
        
        def can_not_build(self):
            pass
        
        def buf_debaf(self):
            pass

class Screen(Game):
    X_glob = 0
    Y_glob = 0
    Size = [1060, 600]
    screen = pygame.display.set_mode(Size)
    grass = pygame.image.load(".\MyGame\Group 31.png")
    Size_map = [3780, 1920]

    "Экран ҫӗнетни. Вӑйӑ хирне таврӑнмалла"    
    def update_window(self):
        self.screen.blit(self.grass, (self.X_glob, self.Y_glob))
        for i in range(80):
             for j in range(60):
                  something = self.all_plates[j][i]
                  if type(something) != int:
                       self.screen.blit(something.type, (something.points[0], something.points[1] - 140))
        pygame.display.flip()
    
    "Экрана тата пур объекта та (ҫуртсене, ҫулсене, курсора)куҫарса лартассишӗн яваплӑ функци"
    def move(self, moving):
        tmp_x = self.X_glob
        tmp_y = self.Y_glob
        if self.X_glob + moving[0] <= 0 and self.X_glob + moving[0] >= self.Size[0] - self.Size_map[0]:
            self.X_glob += moving[0]
        if self.X_glob > 0:
            self.X_glob = 0
        if self.X_glob < self.Size[0] - self.Size_map[0]:
            self.X_glob = self.Size[0] - self.Size_map[0]
        if self.Y_glob + moving[0] <= 0 and self.Y_glob + moving[0] >= self.Size[1] - self.Size_map[1]:
            self.Y_glob += moving[1]
        if self.Y_glob > 0:
            self.Y_glob = 0
        if self.Y_glob < self.Size[1] - self.Size_map[1]:
            self.Y_glob = self.Size[1] - self.Size_map[1]
        tmp_x = tmp_x - self.X_glob
        tmp_y = tmp_y - self.Y_glob
        for lines in self.all_plates:
            for something in lines:
                if type(something) != int:
                    something.points[0] -= tmp_x
                    something.points[1] -= tmp_y
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
            #print(points, end=', ')
            self.update_window()
            if type(game.all_plates[points[0]][points[1]]) != int:
                something = game.all_plates[points[0]][points[1]]
                self.screen.blit(something.type, (something.points[0], something.points[1] - 140))
            if game.all_plates[points[0]][points[1]] != 1:
                position = pygame.draw.lines(self.screen, (0,0,0), False,
                    [[x + 120, y + 30], [x + 60, y + 60], [x, y + 30]], 2)
            x = pos[0]
            y = pos[1]
        
        
    
    def drawing(self, points, screen):
        print(0)
        screen.screen.blit(self.type, (points[0], points[1] - 140))

class Objects_for_build(Screen):
        pass

class House(Objects_for_build):
        global game, Sc
        def __init__(self, coords):
            self.coords = coords
            x = coords[0] * 60 + Sc.X_glob
            y = coords[1] * 30 + Sc.Y_glob
            self.points = [x, y]
            self.type = pygame.image.load(".\MyGame\house.png")
            self.game = game
            self.prise = 100
            self.key = "house" 
            self.screen = Sc
            self.dopusc = [0, 2]

        def buy_house(self):
            self.buy()

        def buf_people():
            pass

        def buf_economic():
            pass


class Road(Objects_for_build):
        global game, Sc
        def __init__(self, coords):
            self.coords = [coords[0] - 60, coords[1] - 30]
            self.type = pygame.image.load(".\MyGame\house.png")
            self.game = game
            self.prise = 100
            self.key = "house" 
            self.screen = Sc
            self.dopusc = [0, 2]

        def buy_road(self):
            self.buy()

        def buf_people():
            pass

        def buf_economic():
            pass
            

game = Game()
Sc = Screen()
x = 0
y = 0
x_for_lines = 0
y_for_lines = 0
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
                            Sc.update_window()
            if event.button == 1:
                Sc.mark_plate(event.pos)
                print(x,y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b and prev_x != -2:
            moving = [x + 1, y + 1]
            house = House(moving) # Ошибка в координатах
            Sc.mark_plate([x,y])
            house.buy_house()
            Sc.update_window()
            prev_x = -2
            
    pygame.display.flip()





    