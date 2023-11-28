from game import Game
import pygame
"""
    B экране хранятся:
        Игра           - .game
        X поля         - .X_glob
        Y поля         - .Y_glob
        Размер окна    - .size
        Окно           - .window
        Размер карты   - .size_map
        Карта          - .map
        Предыдущая X   - .prev_x
        Предыдущая Y   - .prev_y
"""
class Screen(Game):

    # Создание экрана с начальными параметрами
    # Требует параметр Game
    # Нет возврата
    def __init__(self, game):
        self.game = game
        self.X_glob = 0
        self.Y_glob = 0
        self.size = [1060, 600]
        self.window = pygame.display.set_mode(self.size)
        self.map = pygame.image.load(".\\resources\Map.png")
        self.size_map = [3780, 1920]
        self.prev_x = -2
        self.prev_y = -2

    # Обновление экрана. Отрисовка всех фиксированных объектов
    # Параметров не требует
    # Нет возврата
    def update_window(self):
        self.window.blit(self.map, (self.X_glob, self.Y_glob))
        for i in range(80):
            for j in range(60):
                tmp = self.game.all_plates[j][i]
                if type(tmp) != int:
                    self.window.blit(tmp.icon, tmp.points_for_build)

    # Пермещение поля на некоторые координаты
    # Требует массив из сдвига по х и сдвига по y
    # возвращает относительный сдвиг
    def move(self, moving):
        tmp_x = self.X_glob
        tmp_y = self.Y_glob
        if self.X_glob + moving[0] <= 0 and self.X_glob + moving[0] >= self.size[0] - self.size_map[0]:
            self.X_glob += moving[0]
        if self.X_glob > 0:
            self.X_glob = 0
        if self.X_glob < self.size[0] - self.size_map[0]:
            self.X_glob = self.size[0] - self.size_map[0]
        if self.Y_glob + moving[0] <= 0 and self.Y_glob + moving[0] >= self.size[1] - self.size_map[1]:
            self.Y_glob += moving[1]
        if self.Y_glob > 0:
            self.Y_glob = 0
        if self.Y_glob < self.size[1] - self.size_map[1]:
            self.Y_glob = self.size[1] - self.size_map[1]
        tmp_x = tmp_x - self.X_glob
        tmp_y = tmp_y - self.Y_glob
        for lines in self.game.all_plates:
            for something in lines:
                if type(something) != int:
                    something.points_for_build[0] -= tmp_x
                    something.points_for_build[1] -= tmp_y
        return [tmp_x, tmp_y]
    
    # Находит ромб по координатам касания
    # Требует координаты
    # Возвращает позицию ромба в матрице
    def get_romb(self, points):
        x = points[0] - self.X_glob
        y = points[1] - self.Y_glob
        if (x // 60 + y // 30) % 2 == 0:
            x_1 = (x // 60) * 60
            y_1 = (y // 30 + 1) * 30
            y_vaive = y_1 + (x_1 - x) * 3 ** 0.5 / 3
            if(y_vaive > y):
                Up = True
            else:
                Up = False
            if Up:
                x_return = x // 60 - 1
                y_return = y // 30 - 1
            else:
                x_return = x // 60
                y_return = y // 30
        else:
            x_1 = (x // 60) * 60
            y_1 = (y // 30) * 30
            y_vaive = y_1 + (x - x_1) * 3 ** 0.5 / 3
            if(y_vaive > y):
                Up = True
            else:
                Up = False
            if Up:
                x_return = x // 60
                y_return = y // 30 - 1
            else:
                x_return = x // 60 - 1
                y_return = y // 30
        return [x_return, y_return]
    
    # Выделяет ромб на который нажали. Повторное нажатие убирает выделение
    # Требует координаты
    # Возвращает координаты центра выделенного ромба
    def mark_plate(self, pos):
        points = self.get_romb(pos)
        if points[0] == self.prev_x and points[1] == self.prev_y:
            self.prev_x = -2
            self.prev_y = -2
            self.update_window()
        else:
            self.prev_x = points[0]
            self.prev_y = points[1]
            x = points[0] * 60 + self.X_glob + 60
            y = points[1] * 30 + self.Y_glob + 30
            self.update_window()
            if type(self.game.all_plates[points[0]][points[1]]) != int:
                something = self.game.all_plates[points[0]][points[1]]
                self.window.blit(something.icon, (something.points_for_build[0], something.points_for_build[1]))
            if self.game.all_plates[points[0]][points[1]] != 1:
                pygame.draw.lines(self.window, (0,0,0), False,
                    [[x - 60, y], [x, y + 30], [x + 60, y]], 2)
            
            self.window.blit(pygame.image.load(".\\resources\Menu.png"),(0, 570))
            return[x, y]
        
    # Проверяет возможно ли построить здание
    # Требует постройку
    # Возвращает ошибку либо "True"
    def can_build(self, building):
        points = self.get_romb([building.points_for_build[0] + 60, 
                                building.points_for_build[1] + 170])
        if type(self.game.all_plates[points[0]][points[1]]) != int:
            return "Error_occupied"
        if not(self.game.all_plates[points[0]][points[1]] in building.dopusc):
            return "Error_dopusc"
        if self.game.money < building.prise:
            return "Error_money"
        if (not(type(self.game.all_plates[points[0] - 1][points[1] - 1]).__name__ == "Road"
            or type(self.game.all_plates[points[0] + 1][points[1] - 1]).__name__ == "Road"
            or type(self.game.all_plates[points[0] + 1][points[1] + 1]).__name__ == "Road"
            or type(self.game.all_plates[points[0] - 1][points[1] + 1]).__name__ == "Road")
            and not(type(building).__name__ == "Road")):
            return "Error_no_road"
        return "True"
    
    # Функция покупки здания. Меняет цены, сохраняет данные о здании в матрице
    # Требует объект типа "Строение"
    # Возврата нет
    def buy_building(self, building):
        points = self.get_romb([building.points_for_build[0] + 60, 
                                building.points_for_build[1] + 170])
        self.game.money -= building.prise
        self.game.all_plates[points[0]][points[1]] = building    
    

    # Выводит в центра экрана ошибку, которая закрывается по нажатию
    # Требует название ошибки
    # Возврата нет
    def show_error(self, error_name):                                          # [480 * 250]
        error = pygame.image.load(f".\\resources\Errors\{error_name}.png")
        self.window.blit(error, ((self.size[0] - 480) // 2, 
                                 (self.size[1] - 250) // 2))
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    done = True
        self.update_window()
                
        