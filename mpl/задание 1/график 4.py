# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 19:13:50 2025

@author: User
"""
import matplotlib.pyplot as plt

def read_file(name):
    
    with open(name, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        # Читаем количество точек
        n = int(lines[0])
        # Проверяем соответствие количества данных
        if len(lines) - 1 != n:
            if len(lines) - 1 != n:
                raise ValueError("Ожидалось {n} точек")
    # Записываем в координаты
    x, y = [], []
    for line in lines[1:]:
        parts = line.split()
      
        x.append(float(parts[0]))
        y.append(float(parts[1]))
        
    return x, y
                          
       
def plot (x, y):
    plt.figure(figsize=(15, 6))
    plt.scatter(x, y, color='blue')
    plt.title("Number of points: 238", size=15)
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.savefig("График 4.png")
    plt.axis('equal')  
    plt.grid(True)
    plt.tight_layout()


name = "fig 4.txt"
X, Y = read_file(name) 
plot (X, Y)
  
    
    