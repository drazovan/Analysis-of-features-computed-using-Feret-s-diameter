# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:34:44 2019

@author: Slobodan
"""

from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest, chi2

# chi2 test se moze korisiti samo za kategorical promejive.
# koristimo 

#X, y = load_digits(return_X_y=True)
#X = X[0:300,:]
#y=y[0:300]
X = descriptors.iloc[:,0:10]

y = descriptors.iloc[:,10]

#X_new = SelectKBest(k=3).fit_transform(X, y)

#X_new = SelectKBest(chi2, k=1).fit_transform(X, y)


#X=np.array([[1,400,3,5],[4,500,4,5],[6,300,8,3],[6,300,10,7]])
#Y=np.array([1,1,2,2])
X_new = SelectKBest(k=1).fit_transform(X, y)
#len(X_new)