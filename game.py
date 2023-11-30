from time import time as tm
from random import randint
# from hospital import Hospital
"""
    Глобально:
        Количество больниц              -   hospital_number
        Количество домов                -   house_number
        Количество школ                 -   school_number
        Количество полицейских уч.      -   police_number
        Количество администраций        -   president_number
        Количество университетов        -   university_number
        Количество церквей              -   church_number
        Количество кладбищ              -   cemetery_number
        Количество пожарных станций     -   fire_number
        Количество заводов              -   factory_number
        Количество свалок               -   dump_number
    B игре хранится:
        Количество денег                -   .money
        Текущее время                   -   .time
        Матрицу построек                -   .all_plates

"""
class Game:
    hospital_number = 0 # (4) счетчик госпиталей
    house_number = 0 # (5) счетчик домов
    school_number = 0
    police_number = 0
    president_number = 0
    university_number = 0
    fire_number = 0
    church_number = 0
    cemetery_number = 0
    factory_number = 0
    dump_number = 0
    score = 0
    # Задача начальных параметров, котрые нужны при старте игры.
    # Параметры не требует
    # Нет возврата
    def __init__(self):
        self.prev = tm()
        self.time = 0
        self.money = 10000000
        self.citizens = 0
        self.available_capacity = 0
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
        if (int(self.time) % 20 == 0):
            self.add_citizens()
            self.add_score()
            self.die_monkey() # (2) перенес формулу
            self.check_adjust()
    def pause_time(self):
        self.prev = tm()

    # Добавление жителей
    # На основе разниц между максимальной вместимостью и текущим населением
    # А также обнуление роста при приближении к максимуму
    def add_citizens(self):
        difference = Game.score % 100 // 10 * (self.available_capacity - self.citizens) // randint(20, 50)
        if (difference >= (int(self.available_capacity) - int(self.citizens))): 
            difference = randint(0, (self.available_capacity - self.citizens) )
        self.citizens += difference // 10

    # Подсчет очков от зданий
    # Подсчет вместимости зданий
    # А также обновление счета
    def add_score(self):
        house_capacity = 0
        for i in range(70):
            for j in range(i % 2, 70, 2):
                building = self.all_plates[i][j]
                if type(building) != int:
                    house_capacity += building.get_capacity()
        self.available_capacity = house_capacity

    def check_adjust(self):                
        if self.citizens > 0: # (3) проверка, что кто-то есть иначе там деление на ноль
            self.adjusts_score() # (2) сюда, чтобы до обновления
        

    # Обратное add citizens
    def die_monkey(self):
        if (Game.score > 0):
            death_rate = self.citizens // Game.score // randint(60, 100)
        else:
            death_rate = Game.score * self.citizens // randint(60, 100)
        self.citizens += death_rate // 10

    def adjusts_score(self):
            if (self.citizens - Game.hospital_number * 200 > 0):
                Game.score -= (self.citizens - Game.hospital_number * 200) // 100 # (1) Кайф формула
            else:
                buildings_score = 0
                for i in range(70):
                    for j in range(i % 2, 70, 2):
                        building = self.all_plates[i][j]
                        if type(building) != int:
                            buildings_score += building.get_score()
                Game.score = buildings_score