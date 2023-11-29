from objects_for_build import Objects_for_build
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
    def __init__(self, screen, pos):
        icon = pygame.image.load(".\\resources\\Buildings\House_1.png")
        self.dopusc = [0, 2]
        self.prise = 10000
        super().__init__(screen, pos, icon)
        self.can = self.screen.can_build(self)

    # Покупка здания
    # Параметры не требует
    # Возврата нет
    def buy(self):
        if(self.can == "True"):
            self.screen.buy_building(self)
        else:
            self.screen.show_error(self.can)
        