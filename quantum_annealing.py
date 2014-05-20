# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:23:32 2014

@author: wittek
"""

import matplotlib.pyplot as plt
import numpy as np
from common_graphics_settings import initialize_graphics

colors = initialize_graphics()
fig = plt.figure(1,figsize=(5,5))
ax1 = fig.add_subplot(111)

# Right side of the diagram
domain = np.arange(0.0, 8*np.pi, 0.01)
y3 = [ 10*((2*np.cos(x)+np.log(x+4)-7*np.exp(-(x-15)*(x-15)/100))/3.5) for x in domain ]
line, = ax1.plot(domain, y3, lw=3, color=colors[0])
ax1.annotate('', xy=(11.6, -4), xytext=(9.7, -12.1),
            arrowprops=dict(facecolor=colors[1], shrink=0.05),
            )
plt.text( 11.5, -3.3, 'Thermal\n annealing',fontsize=14)
ax1.annotate('', xy=(14.8, -13.1), xytext=(9.5, -13.1),
            arrowprops=dict(facecolor=colors[2], shrink=0.05),
            )
plt.text( 8.3, -16.5, 'Quantum\n tunneling',fontsize=14)
            
plt.axis('off')
plt.savefig('./quantum_annealing.pdf',bbox_inches='tight')