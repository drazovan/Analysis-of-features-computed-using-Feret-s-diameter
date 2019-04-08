# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:03:57 2019

@author: Slobodan
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# plotting Feret's diameter across over cells and angles

x = np.linspace(1, 368, 368)
y = np.linspace(0, 179, 180)
X, Y = np.meshgrid(x, y)

Z = widthAll.values

fig = plt.figure(figsize=(12,6))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='bone', edgecolor='none');
ax.set_xlabel('cell', fontsize=15, rotation=0, color = '#003366')   
ax.set_ylabel('angle',fontsize=15, rotation=0, color = '#003366')   
ax.set_title('Feret''s diameter over all cells and angles',\
             fontsize=15, rotation=0, color='#003366');
             
ax.view_init(30, 40)
fig

# plotting every descriptor

fig, ax = plt.subplots(figsize=(14,17))
 
plt.subplot(4, 3, 1)
#plt.text(0, 25, r'$\mu=100,\ \sigma=15$')
#plt.text(10, 25, 'ovde moze tekst')
plt.plot(x, maxDiam,color=(0,0,0.35),linestyle='solid')        
plt.title('Maximal Feret''s diameter in px', color=(0.7,0.7,0.8))

plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 2)
plt.plot(x, minDiam,color=(0,0,0.35),linestyle='solid')        
plt.title('Minimal Feret''s diameter in px', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 3)
plt.plot(x, ratio,color=(0,0,0.35),linestyle='solid')        
plt.title('Average Feret''s diameter in px', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 4)
plt.plot(x, meanDiam,color=(0,0,0.35),linestyle='solid')        
plt.title('Aspect ratio', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 5)
plt.plot(x, maxPerpCell,color=(0,0,0.35),linestyle='solid')        
plt.title('Feret''s diameter  perp. to maximal', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 6)
plt.plot(x, minPerpCell,color=(0,0,0.35),linestyle='solid')        
plt.title('Feret''s diameter  perp. to minimal', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 7)
plt.plot(x, FERETvol,color=(0,0,0.35),linestyle='solid')        
plt.title('FERETvol', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 8)
plt.plot(x, bounRectAreaMin,color=(0,0,0.35),linestyle='solid')        
plt.title('Minimal encasing rect. area', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 9)
plt.plot(x, minSide,color=(0,0,0.35),linestyle='solid')        
plt.title('Less side of enc. rect', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 10)
plt.plot(x, maxSide,color=(0,0,0.35),linestyle='solid')        
plt.title('Larger side of enc. rect', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 12)
plt.plot(x, perimeter,color=(0,0,0.35),linestyle='solid')        
plt.title('Perimeter', color=(0.7,0.7,0.8))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

