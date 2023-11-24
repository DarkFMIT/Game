from screen import Screen
class Objects_for_build(Screen):
    def __init__(self, screen, pos, icon):
        self.game = screen.game
        self.screen = screen
        points = screen.get_romb(pos)
        x = points[0] * 60 + screen.X_glob
        y = points[1] * 30 + screen.Y_glob - 140
        self.points_for_build = [x, y]
        self.icon = icon