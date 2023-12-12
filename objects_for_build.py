from screen_opti import Screen
import pygame

"""
    Объекты этого класса не используется
    Необходим для упрощения кода дочерних классов
"""
class Objects_for_build(Screen):
 
    # Инициализация дочернего класса
    # Требует окно, позицию, иконку
    # Возврата нет
    def __init__(self, screen, pos, icon):
        self.game = screen.game
        self.screen = screen
        points = screen.get_romb(pos)
        x = points[0] * 60 + screen.X_glob
        y = points[1] * 30 + screen.Y_glob - 140
        self.points_for_build = [x, y]
        self.icon = icon
    
    def __str__(self) -> str:
        output = type(self).__name__ + "|"
        output += str(self.icon_name) + "|"
        output += str(self.dopusc) + "|"
        output += str(self.dopusc_of_plate) + "|"
        output += str(self.prise) + "|"
        output += str(self.score) + "|"
        output += str(self.capacity) + "|"
        output += str(self.workspace) + "|"
        output += str(self.default_income) + "|"
        output += str(self.can) + "|"
        output += str(self.points_for_build)
        return output
    
    def load(self, str):
        list_of_atributes = str.split("|")
        self.icon_name = list_of_atributes[1]
        icon = pygame.image.load(f"./resources/Buildings/{self.icon_name}.png")
        self.icon = icon
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
        self.default_income = int(list_of_atributes[8])
        self.can = bool(list_of_atributes[9])
        tmp_coords = list_of_atributes[10]
        tmp_coords = tmp_coords.replace("[", "")
        tmp_coords = tmp_coords.replace(",", "")
        tmp_coords = tmp_coords.replace("]", "")
        tmp_coords = tmp_coords.split()
        self.points_for_build = [int(i) for i in tmp_coords]





        