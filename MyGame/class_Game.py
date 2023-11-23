class Game:
        time = 0
        money = 2000000
        file = open('./MyGame/txt.txt', 'r+')
        all_plates = [[0 for i in range(90)] for i in range(90)]
        for i in range(80):
            str = file.readline().split()
            for j in range(len(str)):
                all_plates[i][j] = int(str[j])
                
        def buy(self):
                points = self.get_romb(self.coords)
                print(points)
                if not(self.game.all_plates[points[0]][points[1]] in self.dopusc):
                    self.can_not_build()
                    return 0
                if self.game.money < self.prise:
                    self.need_more_money(self.prise - self.money)
                    return 1
                
                self.money -= self.prise
                self = House(points)   
                self.game.all_plates[points[0]][points[1]] = self     
        
        def randTick(self):
                self.time += 1

        def need_more_money(self, money):
            pass
        
        def can_not_build(self):
            pass
        
        def buf_debaf(self):
            pass