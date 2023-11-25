"""
    В игре хранится:
        Количество денег - .money
        Текущее время    - .time
        Матрицу построек - .all_plates 

"""
class Game:
    # Задача начальных параметров, котрые нужны при старте игры.
    # Параметры не требует
    # Нет возврата
    def __init__(self):
        self.time = 0
        self.money = 100000
        file = open('./txt.txt', 'r+')
        self.all_plates = [[0 for i in range(90)] for i in range(90)]
        for i in range(80):
            str = file.readline().split()
            for j in range(len(str)):
                self.all_plates[i][j] = int(str[j])
