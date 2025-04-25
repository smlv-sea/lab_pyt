# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

# Данные
x1 = [4.0, -7.0, 34.0, 12.0, 8.0, 160.0, 501.0, 498.0, 512.0, 490.0, 507.0]
y1 = [15.0, 19.0, 6.0, 7.0, 34.0, 12.0, 14.0, 7.0, 6.0, -14.0, -25.0]
x2 = [42, 80, 61, 61]
y2 = [0, 0, 19, -18]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
ax[0].scatter(x1,y1, label='fig.1', color='red')
ax[1].scatter(x2,y2, label='fig.2', color='green')

ax[0].set_title("points 11", size=10)
ax[1].set_title("points 4", size=10)


for ax in ax:
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.legend()
    ax.axis('equal')  
    ax.grid(True)
    plt.tight_layout()


plt.subplots_adjust(wspace=0.3, hspace = 0.5)

fig.suptitle("Number of points", size=15)


plt.savefig('График 1,2.png')


