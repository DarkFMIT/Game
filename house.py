from objects_for_build import Objects_for_build
import pygame

"""
    B классе хранятся:
        Иконка                - .icon
        Координаты отрисовки  - .points_for_build
        Допустимые клетки     - .dopusc
        Цена                  - .prise
        Игра                  - .game
        Экран                 - .screen      
"""
class House(Objects_for_build):

    # Создание дома для конкретной клетки
    # Требует окно и координаты
    # Возврата нет
    def __init__(self, screen, pos):
        icon = pygame.image.load(".\house.png")
        self.dopusc = [0, 2]
        self.prise = 1
        super().__init__(screen, pos, icon)

    # Покупка здания
    # Параметры не требует
    # Возврата нет
    def buy(self):
        self.screen.buy_building(self)
        