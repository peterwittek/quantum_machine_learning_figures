import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

from graphics_utils import initialize_graphics, cm2inch

r = rand(8)/5
t = rand(8)
x = r/2 * np.cos(2*np.pi*t) - 0.2
y = r * np.sin(2*np.pi*t) - 0.2
r = rand(40)/5
t = rand(40)
xz = r/2 * np.cos(2*np.pi*t) - 0.2
z = r * np.sin(2*np.pi*t) - 0.2

r = rand(8)/5
t = rand(8)
xx = r * np.cos(2*np.pi*t) + 0.2
yy = r/3 * np.sin(2*np.pi*t)
r = rand(40)/5
t = rand(40)
xzz = r * np.cos(2*np.pi*t) + 0.2
zz = r/3 * np.sin(2*np.pi*t)

colors = initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,10]))
ax.plot(xz, z, 'o',color=colors[0], label='Unlabeled instances')
ax.plot(x, y, 'D', color=colors[1], label='Class 1')
ax.plot(xzz, zz, 'o',color=colors[0])
ax.plot(xx, yy, 's', color=colors[2], label='Class 2')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=4)

plt.axes().set_aspect('equal')
plt.axis('off')

plt.savefig('./transductive.pdf',bbox_inches='tight')
