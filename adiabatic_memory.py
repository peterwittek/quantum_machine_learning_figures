# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:23:32 2014

@author: wittek
"""

import matplotlib.pyplot as plt
import numpy as np
from common_graphics_settings import initialize_graphics

#fig, axes = plt.subplots(2,2)
#((ax1, ax2), (ax3, ax4)) = axes # unpack the axes

colors = initialize_graphics()
fig = plt.figure(1,figsize=(7,5))
ax1 = fig.add_subplot(111, autoscale_on=False, xlim=(0,32), ylim=(-7.5,1.1))

# Right side of the diagram
domain = np.arange(0.0, 8*np.pi, 0.01)
y1 = np.cos(domain)
line, = ax1.plot(domain, y1, lw=3, color=colors[0])
y2 = [ (np.log(x+4)-7*np.exp(-(x-15)*(x-15)/100))/3.5-3 for x in domain ]
line, = ax1.plot(domain, y2, lw=3, color=colors[0])
y3 = [ (np.cos(x)+np.log(x+4)-7*np.exp(-(x-15)*(x-15)/100))/3.5-6 for x in domain ]
line, = ax1.plot(domain, y3, lw=3, color=colors[0])
for i in range(1,9,2):
    ax1.plot(i*np.pi, -0.7, 'o', color=colors[2]) # Stable states in H_mem
ax1.plot(14.7, -3.8, 'o', color=colors[2])        # Stable state in H_inp
ax1.plot(1.06*np.pi, -5.9, 'o', color=colors[2])  # Stable states in the sum
ax1.plot(3.1*np.pi, -6.74, 'o', color=colors[2])
ax1.plot(4.95*np.pi, -7.1, 'o', color=colors[2])
ax1.plot(6.85*np.pi, -6.3, 'o', color=colors[2])

plt.text( 25, -1, '$H_{\mathrm{mem}}$',fontsize=20)
plt.text( 25, -4, '$H_{\mathrm{inp}}$',fontsize=20)
plt.text( 25, -7, '$H_{\mathrm{mem}}+H_{\mathrm{inp}}$',fontsize=20)
            
plt.axis('off')
plt.savefig('./adiabatic_memory.pdf',bbox_inches='tight')