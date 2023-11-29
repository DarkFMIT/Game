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
        self.available_capacity = 0
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
        if (int(self.time) % 10 == 0):
            self.add_citizens()
            self.add_score()

    def pause_time(self):
        self.prev = tm()

    def add_citizens(self):
        difference = self.score % 100 // 10 * (self.available_capacity - self.citizens) // 50
        if (difference >= (int(self.available_capacity) - int(self.citizens))): 
            difference = 0
        self.citizens += difference

    def add_score(self):
        # Подсчет очков от зданий
        building_scores = 0
        house_capacity = 0
        for i in range(70):
            for j in range(i % 2, 70, 2):
                building = self.all_plates[i][j]
                if type(building) != int:
                    building_scores += building.get_score()
                    house_capacity += building.get_capacity()
        
        # Обновление общего счета
        self.score = building_scores
        self.available_capacity = house_capacity