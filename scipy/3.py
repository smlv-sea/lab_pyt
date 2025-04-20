# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 16:53:37 2025

@author: User
"""

'''
Решите диффур два раза - один раз символьно SymPy-ем, второй раз численно SciPy-ем.

Выведите решение, найденное SymPy-ем. Постройте графики: (1) обоих решений на отрезке [0; 10], (2) разности решений SymPy-ем и SciPy-ем на этом же отрезке.
'''

import sympy as sp
from sympy import sqrt, lambdify
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


#Решение диффура с помощью SymPy

x = sp.symbols('x')
y = sp.Function('y')

equation = sp.Eq(y(x).diff(x), -2 * y(x))
ics = {y(0): sqrt(2)}
result_1 = sp.dsolve(equation, y(x), ics=ics)

print(result_1)

#Решение диффура с помощью Scipy

def diffur(x, y): return -2 * y
result_2 = solve_ivp(diffur, [0, 10], [np.sqrt(2)], t_eval=np.linspace(0, 10, 100))

#График

# Подготовка данных
x_sci = result_2.t
y_sci = result_2.y[0]
y_sym_func = lambdify(x, result_1.rhs, 'numpy')
y_sym = y_sym_func(x_sci)

fig, axs = plt.subplots(nrows=1, ncols=2)

axs[0].plot(x_sci, y_sym, label='SymPy', color = 'blue', alpha=0.7)
axs[0].plot(x_sci, y_sci, '--', label='SciPy', color = 'green')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y(x)')
axs[0].set_title('Символьное и численное решения')
axs[0].grid()

axs[1].plot(x_sci, y_sym - y_sci, color='red')
axs[1].set_xlabel('x')
axs[1].set_ylabel('Разность')
axs[1].set_title('Разность решений')
axs[1].grid()

plt.subplots_adjust(wspace = 0.5)

plt.savefig("Решение диффура.png")
