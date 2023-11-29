from time import time as tm
"""
    B игре хранится:
        Количество денег - .money
        Текущее время    - .time
        Матрицу построек - .all_plates 

"""
class Game:
    # Задача начальных параметров, котрые нужны при старте игры.
    # Параметры не требует
    # Нет возврата
    def __init__(self):
        self.prev = tm()
        self.time = 0
        self.money = 100000
        self.citizens = 0
        self.available_space = 0
        self.score = 0
        file = open('./resources/for_map.txt', 'r+')
        self.all_plates = [[0 for i in range(90)] for i in range(90)]
        for i in range(80):
            str = file.readline().split()
            for j in range(len(str)):
                self.all_plates[i][j] = int(str[j])

    # Добавляет время основываясь на раазнице компьютерного времени
    # Параметры не требует
    # Нет возврата
    def add_time(self):
        tmp = tm()
        self.time += 100 * (tmp - self.prev)
        self.prev = tmp

    def pause_time(self):
        self.prev = tm()

    def add_citizens(self):
        self.citizens += self.core % 100 // 10 * (self.available_space - self.citizens)

    def add_available_space(self):
        self.available_space += self.pop

    def add_score(self):
        # Подсчет очков от зданий
        building_scores = sum(building.get_score() for building in self.all_plates)
        
        # Учет количества мест в домах
        house_capacity = sum(building.get_capacity() for building in self.all_plates if isinstance(building, Objects_for_build))
        
        # Обновление общего счета
        self.score = building_scores + house_capacity
