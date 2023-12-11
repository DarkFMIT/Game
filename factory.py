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
class Factory(Objects_for_build):

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
        self.workspace  = 50
        self.default_income = -10
        super().__init__(screen, pos, icon)
        self.can = self.screen.can_build(self)
    
    # Вывод данных класса
    def __str__(self) -> str:
        return super().__str__()

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
        Game.factory_number -= 1 
            
    # Возвращает количество очков, которое приносит это здание
    def get_score(self):
        return self.score

    # Возвращает количество мест в этом здании
    def get_capacity(self):
        return self.capacity
    
    # Возвращает количество рабочих мест
    def get_workplace(self):
        return self.workspace
    
    # Возвращает доход здания
    def get_income(self):
        return self.default_income