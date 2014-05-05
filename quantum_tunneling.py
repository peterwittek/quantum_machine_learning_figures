# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:56:25 2014

@author: wittek
"""
from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np
from graphics_utils import initialize_graphics, cm2inch

def potential_barrier(x,x1,x2,V0):
    if x>x1 and x<x2:
        return V0
    else:
        return 0

def tunneling_wave(x, x1, x2, omega, amplitude1, amplitude2):
    if x<x1:
        return amplitude1*np.sin(2*np.pi*omega*x)
    elif x>x2:
        return amplitude2*np.sin(2*np.pi*omega*x)
    else:
        return 0

x1 = 6.5
x2 = 8.5
V0 = 2
omega = 0.5
amplitude1 = 1
amplitude2 = 0.2

full_range = np.arange(0, 5*np.pi, 0.01)
potential = [ potential_barrier(x, x1, x2, V0) for x in full_range]

until_x1 = np.arange(0.0, x1, 0.01)
wave_until_x1 = [tunneling_wave(t, x1, x2, omega, amplitude1, amplitude2) for t in until_x1]
from_x2 = np.arange(x2+0.01, 5*np.pi, 0.01)
wave_from_x2 = [tunneling_wave(t, x1, x2, omega, amplitude1, amplitude2) for t in from_x2]


colors=initialize_graphics()

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
#fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,5]))

ax.plot(full_range, potential, lw=2, color=colors[2])
ax.plot(until_x1, wave_until_x1, lw=2, color=colors[0])
ax.plot(from_x2, wave_from_x2, lw=2, color=colors[0])

ax.annotate('$U(x)$', xy=(x2, V0), xytext=(x2+0.3, V0-0.2))

ax.set_frame_on(False)
#ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_ticks([x1, x2, 5*np.pi+0.5])
ax.axes.get_xaxis().set_ticklabels(['$x_1$','$x_2$', '$x$'])
ax.axis["xzero"].set_axisline_style("-|>")
ax.axis["xzero"].set_visible(True)
ax.axis["yzero"].set_visible(False)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

ax.set_xlim([-0.5, 5*np.pi+0.5])

plt.savefig('./quantum_tunneling.pdf')
