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
class President(Objects_for_build):

    # Создание административного здания для конкретной клетки
    # Требует окно и координаты
    # Возврата нет
    def __init__(self, screen, pos, icon_name):
        icon = pygame.image.load(f".\\resources\\Buildings\{icon_name}.png")
        self.dopusc = [0, 2]
        self.dopusc_of_plate = 0
        self.prise = 10000
        self.score = 50000
        self.icon_name = icon_name
        self.capacity = 0
        self.workspace = 1000
        self.default_income = -500
        super().__init__(screen, pos, icon)
        self.can = self.screen.can_build(self)
    
    # Вывод данных класса
    # Параметры не требует
    # Возвращает строку
    def __str__(self) -> str:
        return super().__str__()

    # Покупка здания
    # Параметры не требует
    # Возврата нет
    def buy(self):
        if(self.can == "True"):
            self.screen.buy_building(self)
            Game.president_number += 1 
            Game.score += self.score
        else:
            self.screen.show_error(self.can)

    # Удаление здания
    # Парметры не требует
    # Возврата нет
    def goodbuy(self):
        Game.score -= self.score 
        Game.president_number -= 1 
            
    # Возвращает количество очков, которое приносит это здание
    # Парметры не требует
    # Возвращает число
    def get_score(self):
        return self.score

    # Возвращает количество мест в этом здании
    # Парметры не требует
    # Возвращает число
    def get_capacity(self):
        return self.capacity
  
    # Возвращает количество рабочих мест
    # Парметры не требует
    # Возвращает число
    def get_workplace(self):
        return self.workspace
 
    # Возвращает доход здания
    # Парметры не требует
    # Возвращает число
    def get_income(self):
        return self.default_income