import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from numpy.random import rand

from graphics_utils import initialize_graphics, cm2inch

x = rand(40)-0.5
z = x+0.4
y = z+rand(40)/2+0.3
w = z-rand(40)/2-0.3

xx = np.arange(-0.8,0.8,0.01)
yy = xx+0.4

margin_one = xx+0.4+0.2
margin_two = xx+0.4-0.2

colors = initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,10]))
plt.plot(x, y, 'D' , color=colors[0], label='Class 1')
plt.plot(x, w, 's', color=colors[1], label='Class 2')
plt.plot(xx, yy, color=colors[2], linewidth=4, label='Decision\n surface')
plt.plot(xx, margin_one, '--', color=colors[2], linewidth=2, label='Margin')
plt.plot(xx, margin_two, '--', color=colors[2], linewidth=2)

support_vectors_x1 = [-0.4, 0.3]
support_vectors_y1 = [-0.4+0.6, 0.3+0.6]
plt.plot(support_vectors_x1, support_vectors_y1, 'D' , color=colors[0])
for x1, y1 in zip(support_vectors_x1, support_vectors_y1):
    circle1 = Circle((x1, y1), 0.06, facecolor='none', edgecolor=colors[0], linewidth=1)
    ax.add_patch(circle1)

support_vectors_x2 = [-0.1, 0.5]
support_vectors_y2 = [-0.1+0.2, 0.5+0.2]
plt.plot(support_vectors_x2, support_vectors_y2, 's' , color=colors[1])
for x2, y2 in zip(support_vectors_x2, support_vectors_y2):
    circle2 = Circle((x2, y2), 0.06, facecolor='none', edgecolor=colors[1], linewidth=1)
    ax.add_patch(circle2)


handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=4)

plt.axis('off')
ax.set_xlim([-1.1,1.1])
ax.set_ylim([-0.7, 1.5])

plt.savefig('./support_vectors.pdf',bbox_inches='tight')
