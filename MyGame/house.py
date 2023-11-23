from objects_for_build import Objects_for_build
from screen import Sc, game

class House(Objects_for_build):
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

    def buf_people(self):
        pass

    def buf_economic(self):
        pass
