from screen_opti import Screen
from game import Game
import pygame
"""
    B муню хранится:
        Экран               - .screen
        Раздел              - .prev
        Страница            - .page
        Координаты          - .pos
        Основная картинка   - .main_picture
        Массив меню         - .images
        Текст для денег     - .text_money
        Текст для времени   - .text_time
"""
class Menu(Screen):

    # Задача начальных параметров
    # Требует экран
    # Возврата нет
    def __init__(self, screen):
        self.screen = screen
        self.prev = -2
        self.flag = False
        self.num_razd = -2
        self.page = 1
        self.pos = [0, screen.size[1] - 30]
        self.main_picture = pygame.image.load(".\\resources\Menu.png")
        self.images = [[0 for i in range(5)] for i in range(5)]
        self.razdel = [0 for i in range(10)]
        self.init_images()

    # Обновление нижней полоски меню
    # Параметры не требует
    # Нет возврата
    def update_menu(self):
        self.text_money = pygame.font.SysFont('Comic Sans MS', 15).render("$ " + str(self.screen.game.money), False, (0, 0, 0))
        self.screen.window.blit(self.main_picture, self.pos)
        self.screen.window.blit(self.text_money, (10, self.pos[1] + 5))
        
        self.text_citizens = pygame.font.SysFont('Comic Sans MS', 15).render(" citizens " + str((self.screen.game.citizens + self.screen.game.citizens_prev) // 2), False, (0, 0, 0))
        self.screen.game.citizens_prev = (self.screen.game.citizens + self.screen.game.citizens_prev) // 2
        self.screen.window.blit(self.text_citizens, (100, self.pos[1] + 5))

        self.text_available_capacity = pygame.font.SysFont('Comic Sans MS', 15).render(" capacity " + str(self.screen.game.available_capacity), False, (0, 0, 0))
        self.screen.window.blit(self.text_available_capacity, (200, self.pos[1] + 5))

        self.text_score = pygame.font.SysFont('Comic Sans MS', 15).render(" score " + str(Game.score), False, (0, 0, 0))
        self.screen.window.blit(self.text_score, (300, self.pos[1] + 5))

        self.text_workspace = pygame.font.SysFont('Comic Sans MS', 15).render(" workspaces " + str(Game.workspace), False, (0, 0, 0))
        self.screen.window.blit(self.text_workspace, (800, self.pos[1] + 5))

        if Game.income_counter >= 0:
            good = pygame.image.load("./resources/positive_diffirence.png")
            self.screen.window.blit(good, (2, self.pos[1] + 5))
        else:
            bad = pygame.image.load("./resources/negative_diffirence.png")
            self.screen.window.blit(bad, (2, self.pos[1] + 5))

        self.update_time()

    # Обновление времени
    # Параметры не требует
    # Нет возврата
    def update_time(self):
        self.text_time = pygame.font.SysFont('Comic Sans MS', 15).render(Menu.norm_time(self.screen.game.time), False, (0, 0, 0))
        self.screen.window.blit(self.text_time, (self.screen.size[0] - 60, self.pos[1] + 5))
        pygame.display.flip()

    # Переводит время в формат чч:мм
    # Требует время в секундах
    # Возвращают строку формата чч:мм
    def norm_time(seconds):
        tmp = ""
        if int(seconds) // 60 // 60 % 24 < 10:
            tmp = "0" + str(int(seconds) // 60 // 60 % 24)
        else:
            tmp = str(int(seconds) // 60 // 60 % 24)
        tmp += ":"
        if (int(seconds) % (60 * 60)) // 60 < 10:
            tmp += "0" + str((int(seconds) % (60 * 60)) // 60)
        else:
            tmp += str((int(seconds) % (60 * 60)) // 60)
        return tmp
    
    # Вызывает меню построек
    # Требует координаты выделенного ромба
    # Нет возврата
    def dop_menu(self, mark_pos):
        while self.prev != -2:
            self.screen.update_window()
            self.screen.window.blit(self.images[self.prev][self.page], (0, self.pos[1] - 150))
            self.update_menu()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if event.pos[1] > 570:
                            self.choose(event.pos, mark_pos)
                        if event.pos[1] < 570 and event.pos[1] > 420:
                            plate = self.work_with_menu(event.pos)
                            if plate != 0:
                                number = (plate + (self.page - 1) * 4)
                                if number <= self.razdel[self.prev]:
                                    self.number = number
                                    self.flag = True
                                    self.num_razd = self.prev
                                    self.prev = -2
                if event.type == pygame.QUIT:
                    self.prev = -2
        self.screen.game.pause_time()
        self.screen.prev_x = -2
        self.update_menu()
        self.screen.update_window()

    # Определение касаний в меню с иконками
    # Требует координаты касания
    # Нет возврата
    def work_with_menu(self, pos): 
        tmp = 0
        if pos[0] < 60 and self.images[self.prev][self.page - 1] != 0:
            self.page -= 1
        elif pos[0] > 1000 and self.images[self.prev][self.page + 1] != 0:
            self.page += 1
        elif pos[0] > 170 and pos[0] < 320:
            tmp = 1
        elif pos[0] > 360 and pos[0] < 510:
            tmp = 2
        elif pos[0] > 550 and pos[0] < 700:
            tmp = 3
        elif pos[0] > 740 and pos[0] < 890:
            tmp = 4
        return tmp

    # По позиции клика определяет кнопку на нижней понеле
    # Требует позицию и координаты выделенного ромба
    # Нет возврата
    def choose(self, pos, mark_pos):
        if pos[0] > 470 and pos[1] > 570:
            if pos[0] < 510:
                if self.prev == 1:
                    self.prev = -2
                    self.page = 1
                else:
                    self.prev = 1
                    self.page = 1
                    self.dop_menu(mark_pos)
            elif pos[0] < 550:
                if self.prev == 2:
                    self.prev = -2
                    self.page = 1
                else:
                    self.prev = 2
                    self.page = 1
                    self.dop_menu(mark_pos)
            elif pos[0] < 590:
                if self.prev == 3:
                    self.prev = -2
                    self.page = 1
                else:
                    self.prev = 3
                    self.page = 1
                    self.dop_menu(mark_pos)

    # В массив картинок заносит все странички меню
    # Параметры не требует
    # Возврата нет
    def init_images(self):
        self.razdel[1] = 12
        self.razdel[2] = 10
        self.razdel[3] = 9
        self.images[1][1] = pygame.image.load(".\\resources\menus\\1_1.png")
        self.images[1][2] = pygame.image.load(".\\resources\menus\\1_2.png")
        self.images[1][3] = pygame.image.load(".\\resources\menus\\1_3.png")
        self.images[2][1] = pygame.image.load(".\\resources\menus\\2_1.png")
        self.images[2][2] = pygame.image.load(".\\resources\menus\\2_2.png")
        self.images[2][3] = pygame.image.load(".\\resources\menus\\2_3.png")
        self.images[3][1] = pygame.image.load(".\\resources\menus\\3_1.png")
        self.images[3][2] = pygame.image.load(".\\resources\menus\\3_2.png")
        self.images[3][3] = pygame.image.load(".\\resources\menus\\3_3.png")  