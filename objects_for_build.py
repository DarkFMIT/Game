from screen_opti import Screen

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
        