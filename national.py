# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:38:39 2022

@author: 18329
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df= pd.read_csv("C:\\Users\\18329\\Downloads\\Pre_term.csv")
x= df.iloc[:,:-1]
print(x.shape)
y = df.iloc[:,-1:]
print(y.shape)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size= 0.1, random_state=10)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
model = LogisticRegression()
grid={'C':10.0**np.arange(-2,3), 'penalty':['l1','l2']}
cv=KFold(n_splits=5, shuffle=False)
claf= GridSearchCV(model,grid, cv=cv, n_jobs=-1, scoring='f1_macro')
claf.fit(x_train,y_train)
from imblearn.under_sampling import RandomUnderSampler
rus= RandomUnderSampler(random_state=1)
x_train_resampled,y_train_resampled = rus.fit_resample(x_train,y_train)
claf= LogisticRegression(max_iter=1200000).fit(x_train_resampled,y_train_resampled)
y_pred= claf.predict_proba(x_test)[:,1]
y_pred
import pickle 
pickle_out = open('claf.pkl','wb')
pickle.dump(claf,pickle_out)
pickle_out.close()