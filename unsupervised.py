import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
from numpy.random import rand

from graphics_utils import initialize_graphics, cm2inch

r = rand(40)/5
t = rand(40)
x = r * np.cos(2*np.pi*t) - 0.3
y = r * np.sin(2*np.pi*t) - 0.3

r = rand(40)/5
t = rand(40)
xx = r * np.cos(2*np.pi*t) + 0.3
yy = r/3 * np.sin(2*np.pi*t) + 0.3


r = rand(40)/5
t = rand(40)
xxx = r/2 * np.cos(2*np.pi*t) - 0.15
yyy = r * np.sin(2*np.pi*t) + 0.15

colors = initialize_graphics()
circle1 = Ellipse((-0.3, -0.3), 0.42, 0.42, facecolor='none', edgecolor=colors[1], linewidth=4, label='Decision boundary')
circle2 = Ellipse((0.3, 0.3), 0.42, 0.22, facecolor='none', edgecolor=colors[1], linewidth=4)
circle3 = Ellipse((-0.15, +0.15), 0.22, 0.42, facecolor='none', edgecolor=colors[1], linewidth=4)

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,10]))
plt.plot(x, y, 'o', color=colors[0], label='Unlabeled instances')
plt.plot(xx, yy, 'o', color=colors[0])
plt.plot(xxx, yyy, 'o', color=colors[0])

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=4)

plt.axes().set_aspect('equal')
plt.axis('off')
ax.set_xlim([-0.52, 0.52])
ax.set_ylim([-0.52, 0.52])

plt.savefig('./unsupervised.pdf',bbox_inches='tight')
