# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:23:32 2014

@author: wittek
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
from graphics_utils import initialize_graphics, cm2inch

x = np.arange(0.0, 10*np.pi, 0.01)
y = np.cos(x)

colors=initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,10]))

ax.plot(x, y, lw=3, color=colors[0])
for i in range(0,11,2):
    ax.plot(i*np.pi + 2*(rand(1)-0.5), -0.1, 'o', color=colors[1])
for i in range(1,11,2):
    ax.plot(i*np.pi + 2*(rand(1)-0.5), -0.1, 'D', color=colors[2])


ax.set_ylim([-1.5, 1.5])
            
plt.axis('off')

plt.savefig('./vc_dimension_sine.pdf',bbox_inches='tight')