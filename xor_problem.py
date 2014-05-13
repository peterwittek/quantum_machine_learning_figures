import matplotlib.pyplot as plt
import numpy as np

from graphics_utils import initialize_graphics, cm2inch


xx = np.arange(-0.1, 1.1,0.01)
yy = -xx+0.9

x1 = [0, 1]
y1 = [1, 0]
x2 = [1 ,0]
y2 = [1, 0]

colors = initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,10]))
plt.plot(x1, y1, 'D' , color=colors[0], label='Class 1')
plt.plot(x2, y2, 's', color=colors[1], label='Class 2')
plt.plot(xx, yy, color=colors[2], linewidth=4, label='Decision\n surface')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=7)

plt.axis('off')
ax.set_ylim([-0.1, 1.1])

plt.savefig('./xor_problem.pdf',bbox_inches='tight')
