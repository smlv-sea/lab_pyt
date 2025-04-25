# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 18:45:06 2025

@author: User
"""

import matplotlib.pyplot as plt

# Это будут наши данные
x1 = [42, 188, 61, 61]
y1 = [0, 2, 19, -18]

# Форма пространства и сам график
plt.figure(figsize=(12, 6))
plt.scatter(x1,y1, label='fig.3', color='black')

# Название осей
plt.xlabel('x label')
plt.ylabel('y label')

# Название графика
plt.title("Number of points: 4")

# Нарисуем легенду
plt.legend()
plt.axis('equal')  
plt.grid(True)
plt.tight_layout()

# Задаёт количество точек на оси
plt.locator_params(axis='y', nbins=5)
plt.locator_params(axis='x', nbins=7)


# Сохраним график
plt.savefig("График 3.png")