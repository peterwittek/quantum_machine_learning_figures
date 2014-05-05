# -*- coding: utf-8 -*-
"""
Created on Mon May  5 14:15:02 2014

@author: wittek
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from qutip import Bloch
from graphics_utils import initialize_graphics

colors = initialize_graphics()

fig = plt.figure()
axes = Axes3D(fig)
axes.grid = True
axes.axis("off")
axes.set_axis_off()

b=Bloch()

b.fig = fig
b.axes = axes
#b.fig = fig
#b.frame_width=1
b.sphere_color = 'white'
b.sphere_alpha = 0.1
#b.size = [10, 10]
b.make_sphere()

plt.savefig('./bloch_sphere.svg',bbox_inches='tight')
#b.show()
#b.save('bloch_sphere.pdf',format='pdf')
