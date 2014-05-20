import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

from graphics_utils import initialize_graphics, cm2inch

def zero_one(x):
    if x<0:
        return 1
    else:
        return 0

def savage_loss(x):
    return 4/(1+np.exp(2*x))**2

def tangent_loss(x):
    return (2*np.arctan(x)-1)**2

x = np.arange(-6,8,0.01)
y_zero_one = [zero_one(t) for t in x]
y_savage_loss = [savage_loss(t) for t in x]
y_tangent_loss = [tangent_loss(t) for t in x]
colors = initialize_graphics()

fig, ax = plt.subplots()
fig.set_size_inches(cm2inch([10,7]))
plt.plot(x, y_zero_one, color='black', linewidth=3, label='Zero-one')
plt.plot(x, y_savage_loss, color=colors[0], linewidth=2, label='Savage loss')
plt.plot(x, y_tangent_loss, '--', color=colors[1], linewidth=2, label='Tangent loss')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=1)

#plt.axis('off')
ax.set_xlim([-5, 8])
ax.set_ylim([0, 15])

plt.savefig('./nonconvex_loss_functions.pdf',bbox_inches='tight')
