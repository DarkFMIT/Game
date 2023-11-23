from objects_for_build import Objects_for_build
from screen import Sc, game

class Road(Objects_for_build):
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