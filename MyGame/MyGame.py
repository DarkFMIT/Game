import pygame
pygame.init()
class Game:
    time = 0
    money = 200000
    all_plates = [[0 for i in range(41)] for i in range(17)]
    already_bought = {}
    objects = {}
    def buy(self, cost):
        self.money -= cost
    def randTick(self):
        self.time += 1

class Screen(Game):
    X_glob = 0
    Y_glob = 0
    screen = pygame.display.set_mode((1060, 600))
    grass = pygame.image.load(".\MyGame\grass.jpg")
    def update_window(self):
        self.screen.blit(self.grass, (self.X_glob, self.Y_glob))
        for key in self.already_bought.keys():
            for points in self.already_bought[key]:
                self.screen.blit(self.objects[key], (points[0], points[1]))
        pygame.display.flip()
    def move(self, moving):
        tmp_x = self.X_glob
        tmp_y = self.Y_glob
        if self.X_glob + moving[0] <= 0 and self.X_glob + moving[0] >= 1060 - 2500:
            self.X_glob += moving[0]
        if self.X_glob > 0:
              self.X_glob = 0
        if self.X_glob < 1060-2500:
              self.X_glob = 1060-2500
        if self.Y_glob + moving[0] <= 0 and self.Y_glob + moving[0] >= 600 - 1500:
            self.Y_glob += moving[1]
        if self.Y_glob > 0:
              self.Y_glob = 0
        if self.Y_glob < 600-1500:
              self.Y_glob = 600-1500
        tmp_x = tmp_x - self.X_glob
        tmp_y = tmp_y - self.Y_glob
        for key in self.already_bought.keys():
            for i in range(len(self.already_bought[key])):
                self.already_bought[key][i][0] -= tmp_x
                self.already_bought[key][i][1] -= tmp_y
        return [tmp_x, tmp_y]


def get_romb(points):
    x = points[0]
    y = points[1]
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


game = Game()
Sc = Screen()
x = 0
y = 0 
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
                    print(events)
                    if(len(events) != 0):
                        if pygame.mouse.get_pressed()[2] == 0:
                            break
                        else:
                            moving = pygame.mouse.get_rel()
                            moving = Sc.move(moving)
                            x = x - moving[0]
                            y = y - moving[1]
                            Sc.update_window()
            if event.button == 1:
                pos = event.pos
                points = [0, 0]
                points[0] = pos[0] - Sc.X_glob
                points[1] = pos[1] - Sc.Y_glob
                points = get_romb(points)
                x = points[0] * 60 + Sc.X_glob
                y = points[1] * 30 + Sc.Y_glob
                Sc.update_window()
    position = pygame.draw.lines(Sc.screen, (0,0,0), True,
                  [[x + 60, y], [x + 120, y + 30], [x + 60, y + 60], [x, y + 30]], 2)
    pygame.display.flip()