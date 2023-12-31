from time import time as tm
from pygame import image
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
    hospital_capacity = 2000
    hospital_coeff = 100

    house_number = 0

    school_number = 0
    school_capacity = 10000
    school_coeff = 100

    police_number = 0
    police_capacity = 20000
    police_coeff = 100

    president_number = 0

    university_number = 0
    university_capacity = 80000
    university_coeff = 1000

    firestation_number = 0
    firestation_capacity = 8000
    firestation_coeff = 100

    church_number = 0
    church_capacity = 20000
    church_coeff = 10000

    cemetery_number = 0
    cemetery_capacity = 10000
    cemetery_coeff = 100

    factory_number = 0
    facatory_capacity = 200

    dump_number = 0
    dump_capacity = 10000
    dump_coeff = 100

    pump_number = 0
    pump_capacity = 20000
    pump_coeff = 100

    score = 0

    workspace = 0

    taxes = 10

    income_counter = 0

    salary = 1

    # Задача начальных параметров, котрые нужны при старте игры.
    # Параметры не требует
    # Нет возврата
    def __init__(self):
        self.prev = tm()
        self.time = 0
        self.money = 60000
        self.citizens = 0
        self.citizens_prev = 0
        self.available_capacity = 0
        self.debuf_warning = image.load("./resources/Warnings/empty.png")
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
        if (int(self.time) % 100 == 0):
            self.add_score()
            self.add_money()
        if (int(self.time) % 20 == 0):
            self.add_citizens()
            if self.citizens > 0:
                self.die_monkey() # (2) перенес формулу
            self.check_adjust()
        if (self.citizens <= 0 and self.available_capacity != 0):
            self.citizens = 2
        
    def pause_time(self):
        self.prev = tm()

    # Добавление жителей
    # На основе разниц между максимальной вместимостью и текущим населением
    # А также обнуление роста при приближении к максимуму
    def add_citizens(self):
        if self.citizens > self.available_capacity:
            self.citizens = self.available_capacity
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
            # Больницы
            hospital_avaiability = self.citizens - Game.hospital_number * Game.hospital_capacity

            # Церкви
            church_avaiability = self.citizens - Game.church_number * Game.church_capacity

            # Полиция
            police_avaiability = self.citizens - Game.police_number * Game.police_capacity

            # Пожарные станции
            firestation_avaiability = self.citizens - Game.firestation_number * Game.firestation_capacity

            # Кладбища
            cemetery_avaiability = self.citizens - Game.cemetery_number * Game.cemetery_capacity

            # Свалка
            dump_avaiability = self.citizens - Game.dump_number * Game.dump_capacity

            # Школы
            school_avaiability = self.citizens - Game.school_number * Game.school_capacity

            # Университеты
            university_avaiability = self.citizens - Game.university_number * Game.university_capacity

            # Водокачка
            pump_avaiability = self.citizens - Game.pump_number * Game.pump_capacity

            # Проверка больницы
            # Не требует населения
            if (hospital_avaiability // Game.hospital_coeff > 0):
                Game.score -= hospital_avaiability // Game.hospital_coeff
                self.debuf_warning = image.load("./resources/Warnings/hospital.png")
            
            # Проверка церкви
            # Требует 15.000 населения
            elif (church_avaiability // Game.church_coeff > 0 and self.citizens > 15000):
                Game.score -= church_avaiability // Game.church_coeff
                self.debuf_warning = image.load("./resources/Warnings/Church.png")

            # Проверка полиции
            # Требует 3.000 населения
            elif (police_avaiability // Game.police_coeff > 0 and self.citizens > 3000):
                Game.score -= police_avaiability // Game.police_coeff
                self.debuf_warning = image.load("./resources/Warnings/Police.png")

            # Проверка пожарной станции
            # Требует 8.000 населения
            elif (firestation_avaiability // Game.firestation_coeff > 0 and self.citizens > 8000):
                Game.score -= firestation_avaiability // Game.firestation_coeff
                self.debuf_warning = image.load("./resources/Warnings/Firestation.png")

            # Проверка кладбища
            # Требует 3.000 населения
            elif (cemetery_avaiability // Game.cemetery_coeff > 0 and self.citizens > 3000):
                Game.score -= cemetery_avaiability // Game.cemetery_coeff
                self.debuf_warning = image.load("./resources/Warnings/Cemetery.png")

            # Проверка школы
            # Требует 10.000 населения
            elif (school_avaiability // Game.school_coeff > 0 and self.citizens > 10000):
                Game.score -= school_avaiability // Game.school_coeff
                self.debuf_warning = image.load("./resources/Warnings/School.png")

            # Проверка свалки
            # Требует 3.000 населения
            elif (dump_avaiability // Game.dump_coeff > 0 and self.citizens > 3000):
                Game.score -= dump_avaiability // Game.dump_coeff
                self.debuf_warning = image.load("./resources/Warnings/Dump.png")

            # Проверка водокачки
            # Не требует населения
            elif (pump_avaiability // Game.pump_coeff > 0):
                Game.score -= pump_avaiability // Game.pump_coeff
                self.debuf_warning = image.load("./resources/Warnings/Water.png")

            # Проверка универа
            # Требует 20.000 населения
            elif (university_avaiability // Game.university_coeff > 0 and self.citizens > 20000):
                Game.score -= university_avaiability // Game.university_coeff
                self.debuf_warning = image.load("./resources/Warnings/School.png")

            # Если всё хорошо, то возвращаем деньги
            else:
                self.debuf_warning = image.load("./resources/Warnings/empty.png")
                buildings_score = 0
                for i in range(70):
                    for j in range(i % 2, 70, 2):
                        building = self.all_plates[i][j]
                        if type(building) != int:
                            buildings_score += building.get_score()
                Game.score += abs(Game.score - buildings_score) // 100

    def add_money(self):
        Game.income_counter = 0
        buildings_workpace = 0
        for i in range(70):
                for j in range(i % 2, 70, 2):
                    building = self.all_plates[i][j]
                    if type(building) != int:
                        Game.income_counter += building.get_income()
        for i in range(70):
                for j in range(i % 2, 70, 2):
                    building = self.all_plates[i][j]
                    if type(building) != int:
                        buildings_workpace += building.get_workplace()
        Game.workspace = buildings_workpace
        if Game.workspace > self.citizens // 2 and Game.workspace != 0:
            Game.income_counter += self.citizens // 2 * Game.salary
        elif Game.workspace < self.citizens // 2 and Game.workspace != 0:
            Game.income_counter += Game.workspace * Game.salary
        self.money += int(Game.income_counter)     

    def load(self, str):
        list_atributes = str.split("|")
        self.time = float(list_atributes[0])
        self.money = int(list_atributes[1])
        self.citizens = int(list_atributes[2])
        self.citizens_prev = int(list_atributes[3])
        self.available_capacity = int(list_atributes[4])
        Game.dump_number  = int(list_atributes[5])
        Game.pump_number = int(list_atributes[6])
        Game.house_number = int(list_atributes[7])
        Game.church_number = int(list_atributes[8])
        Game.police_number = int(list_atributes[9])
        Game.school_number = int(list_atributes[10])
        Game.factory_number = int(list_atributes[11])
        Game.cemetery_number = int(list_atributes[12])
        Game.hospital_number = int(list_atributes[13])
        Game.president_number = int(list_atributes[14])
        Game.university_number = int(list_atributes[15])
        Game.firestation_number = int(list_atributes[16])
    
    def __str__(self):
        output = ""
        output += str(self.time) + "|"
        output += str(self.money) + "|"
        output += str(self.citizens) + "|"
        output += str(self.citizens_prev) + "|"
        output += str(self.available_capacity) + "|"
        output += str(Game.dump_number) + "|"
        output += str(Game.pump_number) + "|"
        output += str(Game.house_number) + "|"
        output += str(Game.church_number) + "|"
        output += str(Game.police_number) + "|"
        output += str(Game.school_number) + "|"
        output += str(Game.factory_number) + "|"
        output += str(Game.cemetery_number) + "|"
        output += str(Game.hospital_number) + "|"
        output += str(Game.president_number) + "|"
        output += str(Game.university_number) + "|"
        output += str(Game.firestation_number)
        return output

