# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:48:01 2014

@author: wittek
"""

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import rc

FONT_SIZE=27.5  
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
      tick.label1.set_fontsize(0.85*FONT_SIZE)
      tick.tick1line.set_markeredgewidth(MP_LINEWIDTH)
      tick.tick1line.set_markersize(0.5*MP_TICKSIZE)
    for tick in plt.gca().yaxis.get_major_ticks():
      tick.label1.set_fontsize(0.85*FONT_SIZE)
      tick.tick1line.set_markeredgewidth(MP_LINEWIDTH)
      tick.tick1line.set_markersize(0.5*MP_TICKSIZE)
    legend = ax.legend(loc='upper left', shadow=False, handlelength=5)
    
    # Set the fontsize in legend
    for label in legend.get_texts():
        label.set_fontsize(FONT_SIZE)
