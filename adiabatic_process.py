# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:23:32 2014

@author: wittek
"""

import matplotlib.pyplot as plt
import numpy as np
from graphics_utils import initialize_graphics

#fig, axes = plt.subplots(2,2)
#((ax, ax2), (ax3, ax4)) = axes # unpack the axes

colors=initialize_graphics()
fig = plt.figure(1,figsize=(10,5))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-33.3,26), ylim=(-7.43,1.1))

# Right side of the diagram
x = np.arange(0.0, 8*np.pi, 0.01)
y = [ (3*np.cos(t)+np.log(t+4)-10*np.exp(-(t-15)*(t-15)/100))/3.5-4.5 for t in x ]
ax.plot(x, y, lw=3, color=colors[0])
ax.plot(4.98*np.pi, -6.95, 'o', color=colors[2])

plt.text( 25, -7, '$H_1$',fontsize=20)

# Left side of the diagram
offset=25

x = np.arange(-8-offset, 8-offset, 0.01)
y4 = [ (t+offset)**2/20-2.5 for t in x]
ax.plot(x, y4, lw=3, color=colors[0])
y5 = [ (t+offset)**2/20-7.4 for t in x]
ax.plot(x, y5, lw=3, color=colors[0])

ax.plot(-31, 0, 'o', color=colors[2])
ax.plot(-offset, -7, 'o', color=colors[2])

#plt.text( -17, -2, '$H_1$',fontsize=20)
plt.text( -17, -7, '$H_0$',fontsize=20)

ax.annotate('', xy=(-offset, -4), xytext=(-offset, -2.7),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax.annotate('', xy=(-3 ,-6), xytext=(-13, -6),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
            
plt.axis('off')
plt.savefig('./adiabatic_process.pdf',bbox_inches='tight')