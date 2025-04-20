# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 21:59:15 2025

@author: User
"""

''' Задание
У вас есть набор показаний, снятых с датчиков. Предполагается, что вообще-то в данных есть какие-то осмысленные сигналы, по которым можно проследить зависимости. К сожалению, данные очень сильно зашумлены.

К счастью, со случайными шумами можно неплохо бороться, усредняя сигнал по времени. Этим и предстоит заняться.

Данные здесь. В каждом файле просто набор значений, полученных в последовательные моменты времени.

Задача - применить к данным фильтр, отрисовать исходные и отфильтрованные данные. Логика фильтра следующая:

    будем использовать простое скользящее среднее с шагом 10,
    смотреть будем только назад по времени,
    стартовые точки сгладим максимально доступным образом.

То есть 0-вое показание остаётся просто собой, 1-ое показание становится средним 0-го и 1-го, 2-ое показание становится средним показаний от 0-го до 2-го и т.д. Показание N становится средним показаний от N-9 до N включительно.
'''

import numpy as np
import matplotlib.pyplot as plt
import os

        
#фильтрация
def average(data, step =10):
    sort = np.zeros_like(data, dtype=float)
    for i in range(len(data)):
        start = max(0, i - step + 1) # до 10 элемента получаем шаг меньше 10
        sort[i] = np.mean(data[start:i+1])
    return sort

#просто данные
def read_data(filename):
    with open(filename, 'r') as f:
        return np.array([float(line.strip()) for line in f])
    
    
txt_files = [f for f in os.listdir() if f.endswith('.txt')]
if not txt_files:
    print("В директории нет файлов .txt")
else:
    for filename in txt_files:
        # Загрузка и фильтрация данных
        original_data = read_data(filename)  
        sort_data = average(original_data)
        
        # Визуализация результатов
        plt.figure(figsize=(16, 6))
        plt.plot(original_data, label='Исходные данные', alpha=0.8, color = 'pink')
        plt.plot(sort_data, label='Отфильтрованные данные', linewidth=2, color = 'red')
        plt.title('Сравнение исходных и отфильтрованных данных')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(-1, 100)
        plt.ylim(0, 35)
        plt.legend()
        plt.grid()
        plt.savefig(f'{filename}.png')
        print(f"График {filename} сохранен")






