import numpy as np
import matplotlib
import matplotlib.pyplot as pl
import scipy as sp
from scipy import stats
from matplotlib.patches import Rectangle
import matplotlib.colors as colors
import matplotlib.cm as cmx
from matplotlib.widgets import Slider, Button, RadioButtons
from mpl_toolkits.axes_grid1 import make_axes_locatable
from PIL import Image
import matplotlib.ticker as plticker
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def display(my_tpfs, my_fpfs, mags, ld_separations,val=10):
    
    fig, ax = pl.subplots() #figsize=(10,18)
    matplotlib.rcParams.update({'font.size': 18})
    currentAxis = pl.gca()
    #fig.subplots_adjust(bottom=0.2)
    ax.set_xticks(np.arange(1.5,4.5,1), minor=True)
    ax.xaxis.grid(True, which='minor', linestyle='-', color='k', linewidth=2)
    ax.set_yticks(np.arange(11.75,14.5,0.5), minor=True)
    ax.yaxis.grid(True, which='minor', linestyle='-', color='k', linewidth=2)
    ss,mm = np.meshgrid(np.arange(11.75,14.5,0.25),np.arange(1.5,5.0,0.5))
    cm1 = ax.imshow(np.transpose(my_tpfs[:,:,(np.abs(my_fpfs-val)).argmin()]), interpolation='nearest',cmap=pl.get_cmap('jet'), vmin=0, vmax=1,extent=(mm.min(),mm.max(),ss.max(),ss.min()))
    pl.xticks(np.arange(2,5.0,1.0))
    pl.xlabel('Separation [$\lambda/$D]',fontsize=20)
    pl.ylabel('$\Delta$mag',fontsize=20)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.25)
    cb = fig.colorbar(cm1, cax)
    cb.set_label("Completeness",labelpad=15, fontsize=20)

    #ax2  = fig.add_axes([0.135, 0.05, 0.7, 0.03])
    #slider = Slider(ax2, 'FPF: ', my_fpfs[0], 0.5, valinit=0.01) #my_fpfs[-1]
    #pl.gca().invert_yaxis()

    #def update(val):
    #ax.imshow(np.transpose(my_tpfs[:,:,(np.abs(my_fpfs-val)).argmin()]),interpolation='nearest',cmap=pl.get_cmap('jet'), vmin=0, vmax=1,extent=(mm.min(),mm.max(),ss.max(),ss.min()))

    #slider.on_changed(update)
    pl.show()
