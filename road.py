from objects_for_build import Objects_for_build
import pygame

class Road(Objects_for_build):

    def __init__(self, screen, pos):
        icon = None
        points = screen.get_romb(pos)
        self.dopusc = [0, 2]
        self.prise = 1
        super().__init__(screen, pos, icon)
        self.icon = self.choose_icon(points)
    def choose_icon(self, points):
        icon_type = ""
        plate = self.game.all_plates[points[0] - 1][points[1] - 1]
        if type(self) == type(plate):
            icon_type += '1'
            plate.rechoose_icon(points)
        else:
            icon_type += '0'
        plate = self.game.all_plates[points[0] - 1][points[1] + 1]
        if type(self) == type(plate):
            icon_type += '1'
            plate.rechoose_icon(points)
        else:
            icon_type += '0'
        plate = self.game.all_plates[points[0] + 1][points[1] + 1]
        if type(self) == type(plate):
            icon_type += '1'
            plate.rechoose_icon(points)
        else:
            icon_type += '0'
        plate = self.game.all_plates[points[0] + 1][points[1] - 1]
        if type(self) == type(plate):
            icon_type += '1'
            plate.rechoose_icon(points)
        else:
            icon_type += '0'
        icon = pygame.image.load(f".\\roads\{icon_type}.png")
        return icon
    def rechoose_icon(self, points_of_new):
        icon_type = ""
        points = self.screen.get_romb([self.points_for_build[0] + 60, self.points_for_build[1] + 170])
        if (type(self) == type(self.game.all_plates[points[0] - 1][points[1] - 1]) 
            or (points[0] - 1 == points_of_new[0] and points[1] - 1 == points_of_new[1])):
            icon_type += '1'
        else:
            icon_type += '0'
        if (type(self) == type(self.game.all_plates[points[0] - 1][points[1] + 1])
            or (points[0] - 1 == points_of_new[0] and points[1] + 1 == points_of_new[1])):
            icon_type += '1'
        else:
            icon_type += '0'
        if (type(self) == type(self.game.all_plates[points[0] + 1][points[1] + 1])
            or (points[0] + 1 == points_of_new[0] and points[1] + 1 == points_of_new[1])):
            icon_type += '1'
        else:
            icon_type += '0'
        if (type(self) == type(self.game.all_plates[points[0] + 1][points[1] - 1])
            or (points[0] + 1 == points_of_new[0] and points[1] - 1 == points_of_new[1])):
            icon_type += '1'
        else:
            icon_type += '0'
        icon = pygame.image.load(f".\\roads\{icon_type}.png")
        self.icon = icon
    def buy(self):
        self.screen.buy_building(self)
