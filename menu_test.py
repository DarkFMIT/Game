from screen import Screen
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
        self.page = 1
        self.pos = [0, screen.size[1] - 30]
        self.main_picture = pygame.image.load(".\\resources\Menu.png")
        self.images = [[0 for i in range(5)] for i in range(5)]
        self.init_images()

    # Обновление нижней полоски меню
    # Параметры не требует
    # Нет возврата
    def update_menu(self):
        self.text_money = pygame.font.SysFont('Comic Sans MS', 15).render("$ " + str(self.screen.game.money), False, (0, 0, 0))
        self.screen.window.blit(self.main_picture, self.pos)
        self.screen.window.blit(self.text_money, (10, self.pos[1] + 5))
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
    # Параметры не требует
    # Нет возврата
    def dop_menu(self):
        while self.prev != -2:
            self.screen.window.blit(self.images[self.prev][self.page], (0, self.pos[1] - 60))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.choose(event.pos)
                if event.type == pygame.QUIT:
                    self.prev = -2
        self.update_menu()
        self.screen.update_window()

    # По позиции клика определяет кнопку
    # Требует позицию
    # Нет возврата
    def choose(self, pos):
        if pos[0] > 490 and pos[1] > 570:
            if pos[0] < 530:
                if self.prev == 1:
                    self.prev = -2
                    self.page = 1
                else:
                    self.prev = 1
                    self.page = 1
                    self.dop_menu()
            elif pos[0] < 570:
                if self.prev == 2:
                    self.prev = -2
                    self.page = 1
                else:
                    self.prev = 2
                    self.page = 1
                    self.dop_menu()
        if pos[1] < 570 and pos[1] > 510:
            if pos[0] < 60 and self.images[self.prev][self.page - 1] != 0:
                self.page -= 1
            elif pos[0] > 1000 and self.images[self.prev][self.page + 1] != 0:
                self.page += 1

    # В массив картинок заносит все странички меню
    # Параметры не требует
    # Возврата нет
    def init_images(self):
        self.images[1][1] = pygame.image.load(".\\resources\menus\\1_1.png")
        self.images[1][2] = pygame.image.load(".\\resources\menus\\1_2.png")
        self.images[2][1] = pygame.image.load(".\\resources\menus\\2_1.png")
        self.images[2][2] = pygame.image.load(".\\resources\menus\\2_2.png")
        self.images[2][3] = pygame.image.load(".\\resources\menus\\2_3.png")  
