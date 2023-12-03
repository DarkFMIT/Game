from time import time as tm
from random import randint
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
    hospital_number = 0 
    hospital_capacity = 200
    hospital_coeff = 10
    house_number = 0
    school_number = 0
    school_capacity = 200
    school_coeff = 10000
    police_number = 0
    police_capacity = 200
    police_coeff = 10000
    president_number = 0
    university_number = 0
    university_capacity = 200
    university_coeff = 10000
    firestation_number = 0
    firestation_capacity = 200
    firestation_coeff = 100000
    church_number = 0
    church_capacity = 200
    church_coeff = 100000
    cemetery_number = 0
    cemetery_capacity = 200
    cemetery_coeff = 10000
    factory_number = 0
    facatory_capacity = 200
    dump_number = 0
    dump_capacity = 200
    score = 0
    workspace = 0

    # Задача начальных параметров, котрые нужны при старте игры.
    # Параметры не требует
    # Нет возврата
    def __init__(self):
        self.prev = tm()
        self.time = 0
        self.money = 10000000
        self.citizens = 0
        self.citizens_prev = 0
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
        if (int(self.time) % 10 == 0):
            self.add_score()
            print(self.score)
        if (int(self.time) % 20 == 0):
            self.add_citizens()
            if self.citizens > 0:
                self.die_monkey() # (2) перенес формулу
            self.check_adjust()
        if (self.citizens == 0 and self.available_capacity != 0):
            self.citizens = 2
    def pause_time(self):
        self.prev = tm()

    # Добавление жителей
    # На основе разниц между максимальной вместимостью и текущим населением
    # А также обнуление роста при приближении к максимуму
    def add_citizens(self):
        difference = Game.score % 100 // 10 * (self.available_capacity - self.citizens) // randint(20, 25)
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

    def die_monkey(self):
        buildings_score = 0
        for i in range(70):
            for j in range(i % 2, 70, 2):
                building = self.all_plates[i][j]
                if type(building) != int:
                    buildings_score += building.get_score()
        if (Game.score > 0):
            ratio = (Game.score // buildings_score)
        # Применение линейной функции для определения improvement factor
            improvement_factor = 1 - ratio
        # Рассчитываем базовую смертность
            base_death_rate = self.citizens // randint(60, 100)
        # Учитываем влияние улучшений (предполагается, что improvement_factor - это коэффициент улучшения, который может изменяться от 0 до 1)
            improved_death_rate = base_death_rate * (1 - improvement_factor)
            self.citizens -= improved_death_rate // 10
        else:
            death_rate = self.score * self.citizens // randint(60, 70)
            self.citizens += death_rate // 10


    def adjusts_score(self):
            hospital_avaiability = self.citizens - Game.hospital_number * Game.hospital_capacity
            church_avaiability = self.citizens - Game.church_number * Game.church_capacity
            police_avaiability = self.citizens - Game.police_number * Game.police_capacity
            firestation_avaiability = self.citizens - Game.firestation_number * Game.firestation_capacity
            cemetery_avaiability = self.citizens - Game.cemetery_number * Game.cemetery_capacity
            if (hospital_avaiability > 0):
                Game.score -= hospital_avaiability // Game.hospital_coeff
            elif (church_avaiability > 0):
                Game.score -= church_avaiability // Game.church_coeff
            elif (police_avaiability > 0):
                Game.score -= police_avaiability // Game.police_coeff
            elif (firestation_avaiability > 0):
                Game.score -= firestation_avaiability // Game.firestation_coeff
            elif (cemetery_avaiability > 0):
                Game.score -= cemetery_avaiability // Game.cemetery_coeff
            else:
                buildings_score = 0
                for i in range(70):
                    for j in range(i % 2, 70, 2):
                        building = self.all_plates[i][j]
                        if type(building) != int:
                            buildings_score += building.get_score()
                Game.score += buildings_score // 100

    def workspace_counter(self):
        buildings_workpace = 0
        for i in range(70):
                for j in range(i % 2, 70, 2):
                    building = self.all_plates[i][j]
                    if type(building) != int:
                        buildings_workpace += building.get_workspace()
        Game.workspace = buildings_workpace
                
