import pygame
from game import Game

class Screen(Game):
    X_glob = 0
    Y_glob = 0
    Size = [1060, 600]
    screen = pygame.display.set_mode(Size)
    grass = pygame.image.load(".\MyGame\Group 31.png")
    Size_map = [3780, 1920]

    def update_window(self):
        self.screen.blit(self.grass, (self.X_glob, self.Y_glob))
        for i in range(80):
            for j in range(60):
                something = self.all_plates[j][i]
                if type(something) != int:
                    self.screen.blit(something.type, (something.points[0], something.points[1] - 140))
        pygame.display.flip()

    def move(self, moving):
        # ... (ваш код)

    def get_romb(self, points):
        # ... (ваш код)

    def mark_plate(self, pos):
        # ... (ваш код)

    def drawing(self, points, screen):
        print(0)
        screen.screen.blit(self.type, (points[0], points[1] - 140))
