# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:23:32 2014

@author: wittek
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
from graphics_utils import initialize_graphics, cm2inch

x = np.arange(0.0, 10, 0.01)
y = x

colors=initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,10]))

ax.plot(x, y, lw=3, color=colors[0])

ax.plot(5, 6, 'o', color=colors[1])
ax.plot(3, 7, 'o', color=colors[1])
ax.plot(7, 4, 'D', color=colors[2])

ax.set_xlim([-1, 11])
ax.set_ylim([-2, 11])
            
plt.axis('off')

plt.savefig('./vc_dimension_line.pdf',bbox_inches='tight')
