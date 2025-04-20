# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 18:45:06 2025

@author: User
"""
'''
У вас есть набор снятых показаний, которые описывают эволюцию некоторого процесса во времени. Состояние в каждый момент времени представляет из себя график в осях OXY.

Каждый график задан поточечно. Все N кадров процесса хранятся в одном файле, в котором 2N строк. Первая строка - набор x-координат точек, вторая строка - набор y-координат этих точек. И так далее каждая пара строк задаёт точки очередного кадра. Собственно файл здесь.

Задача - считать и отрисовать весь процесс покадрово. 
'''

import matplotlib.pyplot as plt


def read(filename):
 
    #Чтение кадров из файла
    frames = {}
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        
        if len(lines) % 2 != 0: 
            print ("Файл содержит нечётное количество строк") 
            
        for i in range(0, len(lines), 2):
            frame_num = i // 2 + 1
            try:
                x = list(map(float, lines[i].split()))
                y = list(map(float, lines[i+1].split()))
                
                
                frames[frame_num] = {'x': x, 'y': y}
            except ValueError as e:
                print(f"Ошибка в кадре {frame_num}: {str(e)}")
                continue                 
    return frames

    
def save(frames):
# Сохранение кадров
    
    for frame_num, data in sorted(frames.items()):
        fig, ax = plt.subplots(figsize=(10, 6))
        
       
        # Пределы гафика
        ax.set_xlim(0, 16)
        ax.set_ylim(-8.5, 12)
        
        # Настройка сетки
        ax.grid(True, which='both', linestyle=':', linewidth=0.5, alpha=0.7)
        
        # Построение графика
        ax.plot(data['x'], data['y'], color='green',linewidth=2, alpha=0.8)
        
        # Настройка заголовка и подписей
        ax.set_title(f"Кадр_{frame_num:01d}", fontsize=14, pad=20)
        ax.set_xlabel('X координата', fontsize=12)
        ax.set_ylabel('Y координата', fontsize=12)
        
        # Сохранение
        plt.tight_layout()
        plt.savefig(f"кадр_{frame_num:01d}.png", dpi=150, bbox_inches='tight')
        plt.close()
    
    print(f"Сохранено {len(frames)} кадров в папку")

# Наши данные
if __name__ == "__main__":
    # Название файла с данными
    file = "2.txt"
    
    # Обработка данных
    try:
        process = read (file)
        
        if not process:
            print("Файл не содержит данных или произошла ошибка чтения")
        else:
            # сохранение в папку
            save (process)
    except Exception as e:
        print(f"Ошибка: {str(e)}") 