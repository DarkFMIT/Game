from time import time as tm
from random import randint
# from hospital import Hospital
"""
    B игре хранится:
        Количество денег - .money
        Текущее время    - .time
        Матрицу построек - .all_plates 

"""
class Game:
    hospital_number = 0
    house_number = 0
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
            self.die_monkey()
            if self.citizens > 0:
                self.adjusts_score()
    def pause_time(self):
        self.prev = tm()

    # Добавление жителей
    # На основе разниц между максимальной вместимостью и текущим населением
    # А также обнуление роста при приближении к максимуму
    def add_citizens(self):
        difference = self.score % 100 // 10 * (self.available_capacity - self.citizens) // randint(20, 50)
        if (difference >= (int(self.available_capacity) - int(self.citizens))): 
            difference = randint(0, (self.available_capacity - self.citizens) )
        self.citizens += difference

    # Подсчет очков от зданий
    # Подсчет вместимости зданий
    # А также обновление счета
    def add_score(self):
        building_scores = 0
        house_capacity = 0
        for i in range(70):
            for j in range(i % 2, 70, 2):
                building = self.all_plates[i][j]
                if type(building) != int:
                    building_scores += building.get_score()
                    house_capacity += building.get_capacity()
        self.score = building_scores
        self.available_capacity = house_capacity

    # Обратное add citizens
    def die_monkey(self):
        if (self.score > 0):
            death_rate = self.citizens // self.score // randint(60, 100)
        else:
            death_rate = self.score * self.citizens // randint(60, 100)
        self.citizens -= death_rate

    def adjusts_score(self):
        if (Game.hospital_number * 100 / self.citizens  < 1):
            self.score -= 10