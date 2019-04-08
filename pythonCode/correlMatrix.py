# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:19:01 2019

@author: Slobodan
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# correlation matrix

data = descriptors
X = data.iloc[:,0:10]  #independent columns
y = data.iloc[:,10]    #target column i.e price range
#get correlations of each features in dataset
corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(10,10))
#plot heat map
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")
