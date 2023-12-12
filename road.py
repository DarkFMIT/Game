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
        icon_name = "0000"
        points = screen.get_romb(pos)
        self.dopusc = [0, 2]
        self.dopusc_of_plate = 0
        self.prise = 10
        self.score = 10
        self.default_income = -0.1
        self.capacity = 0
        super().__init__(screen, pos, icon)
        self.can = self.screen.can_build(self)
        if(self.can == "True"):
            icon_name, self.icon = self.choose_icon(points)
        self.icon_name = icon_name
    
    # Вывод данных класса
    def __str__(self) -> str:
        return super().__str__()
    
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
        return icon_type, icon
    
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
        self.icon_name = icon_type

    # Покупка здания
    # Параметры не требует
    # Возврата нет
    # Cчетчик госпиталей
    # Cчетчик домов
    def buy(self):
        if(self.can == "True"):
            self.screen.buy_building(self)
            Game.house_number += 1 
            Game.score += self.score
        else:
            self.screen.show_error(self.can)

    # Удаление здания
    def goodbuy(self):
        Game.score -= self.score 
            
    # Возвращает количество очков, которое приносит это здание
    def get_score(self):
        return self.score

    # Возвращает количество мест в этом здании
    def get_capacity(self):
        return 0
    
    # Возвращает количество рабочих мест
    def get_workplace(self):
        return 0
    
    # Возвращает доход здания
    def get_income(self):
        return self.default_income
    
    def load(self, str):
        list_of_atributes = str.split("|")
        self.icon_name = list_of_atributes[1]
        icona = pygame.image.load(f"./resources/roads/{self.icon_name}.png")
        self.icon = icona
        tmp_dopusc = list_of_atributes[2]
        tmp_dopusc = tmp_dopusc.replace("[", "")
        tmp_dopusc = tmp_dopusc.replace(",", "")
        tmp_dopusc = tmp_dopusc.replace("]", "")
        tmp_dopusc = tmp_dopusc.split()
        tmp_dopusc = [int(i) for i in tmp_dopusc]
        self.dopusc = tmp_dopusc
        self.dopusc_of_plate = int(list_of_atributes[3])
        self.prise = int(list_of_atributes[4])
        self.score = int(list_of_atributes[5])
        self.capacity = int(list_of_atributes[6])
        self.workspace = int(list_of_atributes[7])
        self.default_income = float(list_of_atributes[8])
        self.can = bool(list_of_atributes[9])
        tmp_coords = list_of_atributes[10]
        tmp_coords = tmp_coords.replace("[", "")
        tmp_coords = tmp_coords.replace(",", "")
        tmp_coords = tmp_coords.replace("]", "")
        tmp_coords = tmp_coords.split()
        self.points_for_build = [int(i) for i in tmp_coords]