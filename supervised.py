import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

from graphics_utils import initialize_graphics, cm2inch

x = rand(40)-0.5
z = x*x+0.4
y = z+rand(40)/3
w = z-rand(40)/3

xx = np.arange(-0.55,0.55,0.01)
yy = xx*xx+0.4

colors = initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,10]))
plt.plot(x, y, 'D' , color=colors[0], label='Class 1')
plt.plot(x, w, 's', color=colors[1], label='Class 2')
plt.plot(xx, yy, color=colors[2], linewidth=4, label='Decision\n surface')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=4)

plt.axis('off')
ax.set_ylim([-0.2, 0.9])

plt.savefig('./supervised.pdf',bbox_inches='tight')
