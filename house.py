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
class House(Objects_for_build):

    # Создание дома для конкретной клетки
    # Требует окно и координаты
    # Возврата нет
    def __init__(self, screen, pos, icon_name):
        icon = pygame.image.load(f".\\resources\\Buildings\{icon_name}.png")
        self.dopusc = [0, 2]
        self.dopusc_of_plate = 0
        self.prise = 10000
        self.score = 100
        self.icon_name = icon_name
        self.capacity = 200
        self.workspace = 3
        self.default_income = 10
        super().__init__(screen, pos, icon)
        self.can = self.screen.can_build(self)
    
    def __str__(self) -> str:
        return super().__str__()

    # Покупка здания
    # Параметры не требует
    # Возврата нет
    def buy(self):
        if(self.can == "True"):
            self.screen.buy_building(self)
            Game.house_number += 1 # (5) счетчик домов
            Game.score += self.score
        else:
            self.screen.show_error(self.can)
    def goodbuy(self):
        Game.score -= self.score 
        Game.house_number -= 1 # (4) счетчик госпиталей

            
        
    def get_score(self):
        # Возвращает количество очков, которое приносит это здание
        return self.score

    def get_capacity(self):
        # Возвращает количество мест в этом здании хуй
        return self.capacity
    
    def get_workplace(self):
        return self.workspace
    
    def get_income(self):
        return self.default_income
    
    def load(self, str):
        return super().load(str)