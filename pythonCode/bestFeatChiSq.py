# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:41:37 2019

@author: Slobodan
"""
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data = descriptors
X = data.iloc[:,0:10]  #descriptor columns
y = pd.DataFrame(data.iloc[:,10])   #target column (perimeter)

# univariate analysis (chi^2 test)

#apply SelectKBest class to extract top 5 best features
bestfeatures = SelectKBest(k=6).fit_transform(X,y)
#dfscores = pd.DataFrame(bestfeatures.scores_)
dfcolumns = pd.DataFrame(X.columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns],axis=1)
#featureScores.columns = ['Specs','Score']  #naming the dataframe columns
#print(featureScores.nlargest(6,'Score'))  #print 5 best features

#X_new = SelectKBest(score_func=chi2, k=5).fit_transform(X, y)

