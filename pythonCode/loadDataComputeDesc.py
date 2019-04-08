# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:47:52 2019
# filename: loadmatlabdata.py
# description : load in data from a .mat file
@author: Slobodan
"""


import scipy.io as spio
import pandas as pd
import numpy as np
import math

# importing the data
mat = spio.loadmat('widthAllCells.mat')
widthAll = pd.DataFrame(mat['widthAllCells'])

# naming rows and columns
cellNames = ['cell'+str(i) for i in range(1,369)]
angles = ['angle'+str(i) for i in range(0,180)]
widthAll.columns = cellNames
widthAll.index = angles

# perimeter as average Feret's multiplied by \pi (Cauchy's theorem)
perimeter = math.pi*widthAll.mean()

# we obxerve average Feret's diameter
meanDiam = widthAll.mean()

# maximal Feret's
maxDiam = widthAll.max()

# minimal Feret's
minDiam = widthAll.min()

# Aspect ratio (irregular shapes have larger ratio,
# but not neccesarily)
ratio = maxDiam/minDiam


# Feret's diameter in the direction perpendicular to the maxDiam

# we find row index with maximum for every column
rowIndMax = widthAll.idxmax()

locations = pd.Series([widthAll.index.get_loc(x) for x in rowIndMax])
locNew = (locations + 90) % 180

# new locatins for every cell at which Ferets diameter 
#should be taken

NamedIndex  = widthAll.columns
locNew.index = NamedIndex

maxPerpCell=[]

# we take from widthAll values at locations from locNew
for x in widthAll.columns:
    maxPerpCell=pd.Series([widthAll[x][locNew[x]] for x in widthAll.columns])

maxPerpCell.index = NamedIndex


# Feret's diameter in the direction perpendicular to the minDiam

# we find row index with minimum for every column
rowIndMin = widthAll.idxmin()

locations = pd.Series([widthAll.index.get_loc(x) for x in rowIndMin]);
locNew = (locations + 90) % 180

# new locatins for every cell at which Ferets diameter should be taken
NamedIndex  = widthAll.columns
locNew.index = NamedIndex

minPerpCell=[]

# we take from widthAll values at locations from locNew
for x in widthAll.columns:
    minPerpCell=pd.Series([widthAll[x][locNew[x]] for x in widthAll.columns])
minPerpCell.index = NamedIndex
    
diff =  maxPerpCell.values - minDiam.values 

# The equivalent diameter, FERETvol, represents the diameter of a 
# sphere having the same volume as the cylinder constructed by FERETmin 
# as the cylinder diameter and FERETmax as its length.
# the volume of the cylindier with FeretMin/2 as radius and FeretMax as height
cylVol = (((minDiam/2)**2)*math.pi)*maxDiam
# radius of the ball with volume equal to cylVol
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
side1=pd.Series([widthAll[x][bounRectAreaMinInd[x]]\
                 for x in bounRectAreaMinInd.index])
side2 = bounRectAreaMin.values/side1.values 

minSide = np.minimum(side1,side2)
minSide.index  = NamedIndex
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
    
 















