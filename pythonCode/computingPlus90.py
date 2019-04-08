# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:13:18 2019

@author: Slobodan
"""

locations = pd.Series([widthAll.index.get_loc(x) for x in rowIndMax]);
locNew = (locations + 90) % 180

# new locatins for every cell at which Ferets diameter should be taken
NamedIndex  = widthAll.columns
locNew.index = NamedIndex

maxPerpCell=[]

# we take from widthAll values at locations from locNew
for x in widthAll.columns:
    maxPerpCell=pd.Series([widthAll[x][locNew[x]] for x in widthAll.columns])
    
    
    
