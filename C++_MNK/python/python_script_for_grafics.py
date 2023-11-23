import matplotlib.pyplot as plt
from math import log10, floor, ceil
import numpy as np

"""
     Так как скрипт запускает С++, то путь начинается от основного ехе файла
     Создание ехе файла из .ру
     1) pyinstaller .\python_script_for_grafics.py
     2) папку _internal и ехе файл перенести в папку python
     3) запучкать через терминал из папки С++_MNK(./python/NAME_OF_SCRIPT.exe )

     !!Проверка корректности ввода прошла в части С++. Повторная не требуется!!
"""

# Получение названия файла и коэффициентов
file_tmp = open('./python/help_information.txt', 'r')
lines = file_tmp.readlines()
file_tmp.close()
file_name = lines[0][:-1]                              # в конце строки \n нужно обрезать
tmp = lines[1].split()
k, b = float(tmp[0]), float(tmp[1])


# Считываем точки из файла
file_points = open(f'./files/{file_name}', 'r')
points = file_points.readlines()
list_of_x = []
list_of_y = []
for i in points:
     if len(i) != 1:
          tmp = i.split()
          tmp_x, tmp_y = float(tmp[0]), float(tmp[1])
          list_of_x.append(tmp_x)
          list_of_y.append(tmp_y)
    

# Отрисовка графика
plt.rcParams["figure.figsize"] = (8,8)       # Задание размера
plt.grid()                                   # Сетка графика
plt.plot(list_of_x, list_of_y, 'ro', ms = 1) # Точки из файла
x1 = max(0, min(list_of_x) - 4)              # Находим точки графика
x2 = max(list_of_x) + 4                      # ...
y1 = x1 * k + b                              # ...  
y2 = x2 * k + b                              # ...
plt.plot([x1, x2], [y1, y2])                 # График
plt.savefig('Grafic.png')                    # Сохранение графика в виде картинки