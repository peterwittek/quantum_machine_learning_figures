# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:48:01 2014

@author: wittek
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import rc
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes
import seaborn as sns

FONT_SIZE=12
MP_LINEWIDTH = 2.4
MP_TICKSIZE = 20.

def initialize_graphics():
    rcParams.update({'figure.autolayout': True})
    rc('text', usetex=True)
    # Configure palette and plotting to pgf/tikz
    sns.set(style="nogrid")
    return sns.color_palette("colorblind")    

def setup_figure(ax):
    
    # Setting up font sizes
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] ):
        item.set_fontsize(FONT_SIZE)
    
    for tick in plt.gca().xaxis.get_major_ticks():
      tick.label1.set_fontsize(FONT_SIZE)
      tick.tick1line.set_markeredgewidth(MP_LINEWIDTH)
      tick.tick1line.set_markersize(0.5*MP_TICKSIZE)
    for tick in plt.gca().yaxis.get_major_ticks():
      tick.label1.set_fontsize(FONT_SIZE)
      tick.tick1line.set_markeredgewidth(MP_LINEWIDTH)
      tick.tick1line.set_markersize(0.5*MP_TICKSIZE)
    legend = ax.legend(loc='upper left', shadow=False, handlelength=5)
    
    # Set the fontsize in legend
    for label in legend.get_texts():
        label.set_fontsize(FONT_SIZE)


def rotate(fig, degree):
    """Rotation of plot with impossible-to-remove, rotated frame.
    """
    plot_extents = 0, 1, 0, 1
    transform = Affine2D().rotate_deg(degree)
    helper = floating_axes.GridHelperCurveLinear(transform, plot_extents)
    ax = floating_axes.FloatingSubplot(fig, 111, grid_helper=helper)
    fig.add_subplot(ax)
    aux_ax = ax.get_aux_axes(transform)
    return aux_ax


def cm2inch(tupl):
    """Helper function to convert centimeters to inches.
    """
    return tuple(i/2.54 for i in tupl)
