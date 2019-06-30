# ~~~~ MODIFICATION TO EXAMPLE BEGINS HERE ~~~~ #
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *
from scipy.interpolate import griddata

def surface_plot(ss):
    sequence_containing_x_vals = []
    sequence_containing_y_vals = []
    sequence_containing_z_vals = []
    m,n = np.shape(ss)
    for i in range(m):
        for j in range(n):
                sequence_containing_x_vals.append(i)
                sequence_containing_y_vals.append(j)
                sequence_containing_z_vals.append(ss[i][j])
    x = sequence_containing_x_vals
    y = sequence_containing_y_vals
    z = sequence_containing_z_vals

    xyz = {'x': x, 'y': y, 'z': z}

    # put the data into a pandas DataFrame (this is what my data looks like)
    df = pd.DataFrame(xyz, index=range(len(xyz['x'])))

    # re-create the 2D-arrays
    x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
    y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
    x2, y2 = np.meshgrid(x1, y1)
    z2 = griddata((df['x'], df['y']), df['z'], (x2, y2), method='cubic')

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1, cmap='RdPu',
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.title('Meshgrid Created from 3 1D Arrays')
    # ~~~~ MODIFICATION TO EXAMPLE ENDS HERE ~~~~ #

    plt.show()


from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
def scatter_plot(ss):

    sequence_containing_x_vals = []
    sequence_containing_y_vals = []
    sequence_containing_z_vals = []
    m,n = np.shape(ss)
    for i in range(m):
        for j in range(n):
                sequence_containing_x_vals.append(i)
                sequence_containing_y_vals.append(j)
                sequence_containing_z_vals.append(ss[i][j])

    fig = pyplot.figure()
    ax = Axes3D(fig)


    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
    pyplot.show()
