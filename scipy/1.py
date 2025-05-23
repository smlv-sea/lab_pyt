# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 14:13:03 2025

@author: User
"""

'''
Найдите собственные значения матрицы в символьном виде.
'''

import sympy as sp

# Определяем символьные переменные
λ, μ, ρ = sp.symbols('λ μ ρ')

# Создаем матрицу 9x9 из нулей
M = sp.zeros(9)

# Заполняем ненулевые элементы
M[0, 3] = -1/ρ
M[1, 4] = -1/ρ
M[2, 5] = -1/ρ
M[3, 0] = -(λ + 2*μ)
M[4, 1] = (-μ) 
M[5, 2] = (-μ) 
M[6, 0] = -λ
M[8, 0] = -λ

# Вычисляем собственные значения
eigenvalues = M.eigenvals()

# Выводим результат
print("Собственные значения матрицы:")
for val, multiplicity in eigenvalues.items():
    print(f"λ = {val} (кратность {multiplicity})")
    