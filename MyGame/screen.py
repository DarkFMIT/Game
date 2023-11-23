import pygame
from game import Game

class Screen(Game):
    X_glob = 0
    Y_glob = 0
    Size = [1060, 600]
    screen = pygame.display.set_mode(Size)
    grass = pygame.image.load(".\MyGame\Group 31.png")
    Size_map = [3780, 1920]

    def __init__(self, game):
        super().__init__()
        self.game = game

    def update_window(self):
        self.screen.blit(self.grass, (self.X_glob, self.Y_glob))
        for i in range(80):
            for j in range(60):
                something = self.all_plates[j][i]
                if type(something) != int:
                    self.screen.blit(something.type, (something.points[0], something.points[1] - 140))
        pygame.display.flip()

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

    def get_romb(self, points):
        x_return = y_return = 0  # Добавлены эти строки
        global Sc  # Добавлено это
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
