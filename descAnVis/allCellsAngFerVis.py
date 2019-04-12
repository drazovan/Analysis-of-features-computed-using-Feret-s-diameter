# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:03:57 2019

@author: Slobodan
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# plotting Feret's diameter over cells and angles

y = np.linspace(0, 179, 180)
X, Y = np.meshgrid(x, y)
Z = widthAll.values

fig = plt.figure(figsize=(12,6))

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='bone', edgecolor='none');                
ax.set_xlabel( '\ncell', linespacing=1.5, fontsize=14, style='italic', rotation=0,\
              color = '#003366')   
ax.set_ylabel('\nangle', linespacing=1.5, fontsize=14, rotation=0, color = '#003366')   
ax.set_title('Feret\'s diameter over all cells and angles\n',\
             style='italic', fontsize=17, rotation=0, color='black');
ax.view_init(30, 40)