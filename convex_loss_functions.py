import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

from graphics_utils import initialize_graphics, cm2inch

def hinge_loss(x):
    if x>1:
        return 0
    else:
        return 1-x

def zero_one(x):
    if x<0:
        return 1
    else:
        return 0

x = np.arange(-5,8,0.01)
y_least_square = (1-x)**2
y_hinge_loss = [hinge_loss(t) for t in x]
y_boosting = [np.exp(-t) for t in x]
y_zero_one = [zero_one(t) for t in x]

colors = initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,7]))
plt.plot(x, y_zero_one, color='black', linewidth=3, label='Zero-one')
plt.plot(x, y_boosting, color=colors[0], linewidth=2, label='Exponential')
plt.plot(x, y_hinge_loss, '--', color=colors[1], linewidth=2, label='Hinge loss')
plt.plot(x, y_least_square, ':', color=colors[2], linewidth=3, label='Least square')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=4)

#plt.axis('off')
ax.set_xlim([-5, 8])
ax.set_ylim([0, 5])

plt.savefig('./convex_loss_functions.pdf',bbox_inches='tight')
