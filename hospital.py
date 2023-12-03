from objects_for_build import Objects_for_build
from game import Game
import pygame

"""
    B классе хранятся:
        Иконка                - .icon  [120 * 200]
        Координаты отрисовки  - .points_for_build
        Допустимые клетки     - .dopusc
        Цена                  - .prise
        Игра                  - .game
        Экран                 - .screen    
        Можно ли строить      - .can   
"""
class Hospital(Objects_for_build):

    # Создание дома для конкретной клетки
    # Требует окно и координаты
    # Возврата нет
    def __init__(self, screen, pos, icon_name):
        icon = pygame.image.load(f".\\resources\\Buildings\{icon_name}.png")
        self.dopusc = [0, 2]
        self.prise = 10000
        self.score = 500
        self.capacity = 0
        self.workspace = 50
        super().__init__(screen, pos, icon)
        self.can = self.screen.can_build(self)

    # Покупка здания
    # Параметры не требует
    # Возврата нет
    def buy(self):
        if(self.can == "True"):
            self.screen.buy_building(self)
            Game.hospital_number += 1 # (4) счетчик госпиталей
            Game.score += self.score
        else:
            self.screen.show_error(self.can)

    # Возвращает количество очков, которое приносит это здание  
    def get_score(self):
        return self.score

    # Возвращает количество мест в этом здании
    def get_capacity(self):
        return self.capacity
    
    def get_workplace(self):
        return self.workspace