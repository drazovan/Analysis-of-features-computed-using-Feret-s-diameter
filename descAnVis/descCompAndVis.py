# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:47:52 2019
# filename: descCompAndVis.py
# description : loads data, computes, visualizes descriptors
@author: Slobodan
"""

import scipy.io as spio
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

#importing the data
mat = spio.loadmat('widthAllCells.mat')
widthAll = pd.DataFrame(mat['widthAllCells'])

#naming rows and columns
cellNames = ['cell'+str(i) for i in range(1,369)]
angles = ['angle'+str(i) for i in range(0,180)]
widthAll.columns = cellNames
widthAll.index = angles

#perimeter as average Feret's multiplied by \pi (Cauchy's theorem)
perimeter = math.pi*widthAll.mean()

#we observe average Feret's diameter
meanDiam = widthAll.mean()

#maximal Feret's
maxDiam = widthAll.max()

#minimal Feret's
minDiam = widthAll.min()

#Aspect ratio (irregular shapes have larger ratio, but not neccesarily)
ratio = maxDiam/minDiam

#Feret's diameter in the direction perpendicular to the maxDiam

# we find row index with maximum for every column
rowIndMax = widthAll.idxmax() 

locations = pd.Series([widthAll.index.get_loc(x) for x in rowIndMax])
locNew = (locations + 90) % 180

# new locatins for every cell at which Ferets diameter 
#should be taken
NamedIndex  = widthAll.columns
locNew.index = NamedIndex

maxPerpCell=[]

#we take from widthAll values at locations from locNew
for x in widthAll.columns:
    maxPerpCell=pd.Series([widthAll[x][locNew[x]] for x in widthAll.columns])
maxPerpCell.index = NamedIndex

# Feret's diameter in the direction perpendicular to the minDiam

#we find row index with minimum for every column
rowIndMin = widthAll.idxmin()

locations = pd.Series([widthAll.index.get_loc(x) for x in rowIndMin]);
locNew = (locations + 90) % 180

#new locatins for every cell at which Ferets diameter should be taken
NamedIndex  = widthAll.columns
locNew.index = NamedIndex
minPerpCell=[]

#we take from widthAll values at locations from locNew
for x in widthAll.columns:
    minPerpCell=pd.Series([widthAll[x][locNew[x]] for x in widthAll.columns])
minPerpCell.index = NamedIndex   
diff =  maxPerpCell.values - minDiam.values 

#Diameter (FERETvol) of ball having the same volume as the cylinder with radius 
#FeretMin/2 and height FERETmax 
cylVol = (((minDiam/2)**2)*math.pi)*maxDiam
FERETvol = (cylVol*(3/4)*(1/(math.pi)))**1.0/3

#minimum area bounding rectangle
locations1 = pd.Series([widthAll.index.get_loc(x) for x in widthAll.index])
locNew1 = (locations1 + 90) % 180
widthAllTrans90 = widthAll.iloc[locNew1]
widthAllTrans90.index = widthAll.index
boundRectArea = widthAll*widthAllTrans90
bounRectAreaMin = boundRectArea.min()

# sides of the minimum area bounding rectangle
bounRectAreaMinInd = boundRectArea.idxmin()
side1 = pd.Series([widthAll[x][bounRectAreaMinInd[x]]\
                 for x in bounRectAreaMinInd.index])
side2 = bounRectAreaMin.values/side1.values 
minSide = np.minimum(side1,side2)
minSide.index = NamedIndex
maxSide = np.maximum(side1,side2)
maxSide.index = NamedIndex

# in the over 11 descriptors. Final dataFrame
descriptors = pd.concat([maxDiam, minDiam, meanDiam, ratio,  maxPerpCell,\
                         minPerpCell,FERETvol,bounRectAreaMin,\
                         minSide,maxSide,perimeter], axis=1)
descNames = ['maxDiam', 'minDiam', 'meanDiam', 'ratio', 'maxPerpCell',\
             'minPerpCell','FERETvol', 'bounRectAreaMin','minSide','maxSide',\
             'perimeter']
descriptors.columns = descNames

############################################################################
############################################################################
# visualizaion of desriptors

x = np.linspace(1, 368, 368)

fig, ax = plt.subplots(figsize=(14,17))
 
plt.subplot(4, 3, 1)
#plt.text(0, 25, r'$\mu=100,\ \sigma=15$')
#plt.text(10, 25, 'ovde moze tekst')
plt.plot(x, maxDiam,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Maximal Feret''s diameter in $px$', color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 2)
plt.plot(x, minDiam,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Minimal Feret''s diameter in $px$', color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 3)
plt.plot(x, ratio,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Aspect ratio',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 4)
plt.plot(x, meanDiam,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Average Feret''s diameter in $px$',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 5)
plt.plot(x, maxPerpCell,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Fer. diam. perp. to max. in $px$',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 6)
plt.plot(x, minPerpCell,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Fer. diam.  perp. to min. in $px$',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 7)
plt.plot(x, FERETvol,color=(0,0.45,0.25),linestyle='solid')        
plt.title('FERETvol in $px$', color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 8)
plt.plot(x, bounRectAreaMin,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Minimal encasing rect. area in $px^2$',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 9)
plt.plot(x, minSide,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Less side of enc. rect in $px^2$',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 10)
plt.plot(x, maxSide,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Larger side of enc. rect in $px$',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)

plt.subplot(4, 3, 12)
plt.plot(x, perimeter,color=(0,0.45,0.25),linestyle='solid')        
plt.title('Perimeter in $px$',color=(0,0.1,0.2))
plt.grid(color=(0.5,0.5,0.5), linestyle='--', linewidth=0.7)


    
 















