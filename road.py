from objects_for_build import Objects_for_build
from game import Game
import pygame
"""
    B классе хранятся:
        Иконка                - .icon
        Координаты отрисовки  - .points_for_build
        Допустимые клетки     - .dopusc
        Цена                  - .prise
        Игра                  - .game
        Экран                 - .screen  
        Можно ли строить      - .can
"""
class Road(Objects_for_build):

    # Создание дороги для конкретной клетки
    # Требует окно и координаты
    # Возврата нет
    def __init__(self, screen, pos):
        icon = None
        points = screen.get_romb(pos)
        self.dopusc = [0, 2]
        self.dopusc_of_plate = 0
        self.prise = 10
        self.score = 10
        self.default_income = -0.1
        super().__init__(screen, pos, icon)
        self.can = self.screen.can_build(self)
        if(self.can == "True"):
            self.icon = self.choose_icon(points)
    
    # Выбирает иконку для дороги исходя из соседних дорог. Меняет иконуи соседних
    # Запускать только после проверки постройки!!!
    # Требует точки ромба(не хотелось загромаждать)
    # Возвращает корректную иконку
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
        icon = pygame.image.load(f".\\resources\\roads\{icon_type}.png")
        return icon
    
    # Перевыбор иконки дороги
    # Требует координаты ромба новой дороги
    # Возврата нет
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
        icon = pygame.image.load(f".\\resources\\roads\{icon_type}.png")
        self.icon = icon

    # Покупка дороги
    # Параметры не требует
    # Возврата нет
    def buy(self):
        if(self.can == "True"):
            self.screen.buy_building(self)
            Game.score += self.score
        else:
            self.screen.show_error(self.can)
    def goodbuy(self):
        Game.score -= self.score 

    def get_score(self):
        # Возвращает количество очков, которое приносит это здание
        return self.score

    def get_capacity(self):
        # Возвращает количество мест в этом здании хуй
        return 0
    
    def get_workplace(self):
        return 0
    
    def get_income(self):
        return self.default_income